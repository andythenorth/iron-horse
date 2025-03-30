import importlib
import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

from badge import BadgeManager
from train.livery import LiverySupplier
from railtype import RailTypeManager
import global_constants
import utils
from utils import timing

command_line_args = utils.get_command_line_args()

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)

# spritelayer_cargo_modules are dynamic imports later, but registered_spritelayer_cargos wasn't trivial to convert to a dynamic import
from spritelayer_cargos import registered_spritelayer_cargos

spritelayer_cargo_module_names = [
    "intermodal_containers",
    "automobiles",
]

# in the rare case that an unfinished railtype won't init cleanly, comment it out here
railtype_module_names = [
    "lgv",
    "lgv_electrified",
    "metro",
    "narrow_gauge",
    "rail_electrified_ac",
    "rail_electrified_ac_dc",
    "rail_electrified_dc",
    "rail_high_clearance",
]

# comment out any unfinished rosters here as needed
roster_module_names = [
    "ibex",
    "moose",
    "pony",
]


class RosterManager(list):
    """
    Sometimes we want to conveniently expose attributes that span active rosters.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as we also use it when we want a list of active rosters (the instantiated class instance behaves like a list object).
    """

    @timing
    def add_rosters(self, roster_module_names, validate_vehicle_ids=False, run_post_validation_steps=False):
        for roster_module_name in roster_module_names:
            roster_module = importlib.import_module(
                "." + roster_module_name, package="rosters"
            )
            roster = roster_module.main()
            self.append(roster)

        # some actions have to be run after the rosters are all added to RosterManager, to ensure all rosters are present
        for roster in self:
            for (
                livery_name,
                livery_def,
            ) in roster.engine_and_pax_mail_car_liveries.items():
                livery_supplier.add_livery(livery_name, **livery_def)
            roster.produce_engines()
            roster.produce_wagons()

        if validate_vehicle_ids:
            # now validate as we have all the vehicles in all rosters
            # validation will also populate numeric_id_defender which can be re-used for ID reporting
            # actual validation is delegated to the roster
            # quite expensive, so only called if flagged
            self.numeric_id_defender = {}
            for roster in self:
                roster.validate_vehicle_ids(self.numeric_id_defender)

        # now complete any post validation steps
        # can be quite expensive, so only called if flagged
        if run_post_validation_steps:
            self.active_roster.add_buyable_variant_groups()

    @property
    def active_roster(self):
        # special case if we only want the id report, which does not require an active roster
        if command_line_args.grf_name == "id-report-only":
            return None

        for roster in self:
            if roster.grf_name == command_line_args.grf_name:
                return roster
        # roster should always be found by this point, but eh
        raise Exception("RosterManager: no valid roster found for active_roster")

    def get_roster_by_id(self, roster_id):
        for roster in self:
            if roster.id == roster_id:
                return roster
        else:
            raise Exception("RosterManager: no roster found for ", roster_id)

    @property
    def haulage_bonus_engine_id_tree(self):
        # CABBAGE - JUST USE BADGES
        # supports a BAD FEATURE easter egg, where some railcar speeds are increased when hauled by express engine, and can be used as fast MUs
        express_engine_ids = []
        # if we wanted cross-grf haulage bonus then this would need extending beyond active_roster; but we don't as of April 2023, so eh
        for model_variant in self.active_roster.engine_model_variants:
            # check for express-type roles, which are determined by multiple role groups
            for role in [
                "express",
                "driving_cab",
                "express_railcar",
                "high_power_railcar",
            ]:
                subroles = global_constants.role_subrole_mapping[role]
                if model_variant.subrole in subroles:
                    express_engine_ids.append(model_variant.catalogue_entry.unit_variant_ids[0])
        return [(count, id) for count, id in enumerate(express_engine_ids)]

    @property
    def cargo_sprinter_ids(self):
        # CABBAGE - JUST USE BADGES
        # find cargo_sprinters
        # used to switch wagon company colours
        result = []
        # if we wanted cross-grf cargo sprinters then this would need extending beyond active_roster; but we don't as of April 2023, so eh
        for model_variant in self.active_roster.engine_model_variants:
            # abuse the spritelayer_cargo_layers property here, we're just looking for a string, this might be fragile, but eh
            if "cargo_sprinter" in getattr(model_variant, "spritelayer_cargo_layers", []):
                result.append(model_variant.id)
        if len(result) > 255:
            raise BaseException(
                "action 2 switch is limited to 255 values, cargo_sprinter_ids exceeds this - needs split across multiple switches"
            )
        return result


@timing
def main(validate_vehicle_ids=False, run_post_validation_steps=False):
    # exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
    os.makedirs(generated_files_path, exist_ok=True)

    # globals *within* this module so they can be accessed externally by other modules using iron_horse.foo
    globals()["livery_supplier"] = LiverySupplier()
    globals()["badge_manager"] = BadgeManager()
    globals()["railtype_manager"] = RailTypeManager()
    globals()["roster_manager"] = RosterManager()

    # railtypes
    railtype_manager.add_railtypes(railtype_module_names)

    # liveries
    for livery_name, livery_def in global_constants.freight_wagon_liveries.items():
        livery_supplier.add_livery(livery_name, is_freight_wagon_livery=True, **livery_def)

    # rosters
    roster_manager.add_rosters(roster_module_names, validate_vehicle_ids, run_post_validation_steps)

    # spritelayer cargos
    for spritelayer_cargo_module_name in spritelayer_cargo_module_names:
        spritelayer_cargo_module = importlib.import_module(
            "." + spritelayer_cargo_module_name, package="spritelayer_cargos"
        )
        spritelayer_cargo_module.main()

    # badges, done after vehicle models as badges can be either static (global), or dynamically created (for specific vehicle models)

    # CABBAGE - CABBADGE
    # !! badge_manager needs to be encapsulated, it's doing too much here

    if roster_manager.active_roster is not None:
        badge_manager.add_badge(
            "newgrf/" + utils.grfid_to_dword(roster_manager.active_roster.grfid)
        )

    for (
        badge_class_label,
        badge_class_properties,
    ) in global_constants.static_badges.items():
        # first create a badge for the class
        badge_manager.add_badge(
            label=badge_class_label,
            name=badge_class_properties.get("name", None),
        )
        # then create the badges for the class
        for sublabel, sublabel_properties in badge_class_properties.get(
            "sublabels", {}
        ).items():
            badge_manager.add_badge(
                label=badge_class_label + "/" + sublabel,
                name=sublabel_properties.get("name", None),
            )

    for power_source in global_constants.power_sources.keys():
        badge_manager.add_badge(
            label="power_source/" + power_source.lower(),
            name="STR_BADGE_POWER_SOURCE_" + power_source,
        )

    # CABBAGE - CATALOGUES THOUGH?
    # !! this was provably slow as of March 2025, due to walking all variants, but that might be solved now?
    for roster in roster_manager:
        for model_variant in roster.model_variants:
            if model_variant.vehicle_family_badge is not None:
                badge_manager.add_badge(
                    label=model_variant.vehicle_family_badge,
                )

