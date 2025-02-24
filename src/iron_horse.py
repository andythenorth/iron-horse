import importlib
import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

from badge import Badge
from train.livery import LiveryDef
import global_constants
import utils

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


class LiveryManager(dict):
    """
    It's convenient to have a structure for working with liveries.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python dict, as it's a convenient behaviour (the instantiated class instance behaves like a dict object).
    """

    def add_livery(self, livery_name, **kwargs):
        # if not a duplicate, add the livery
        if livery_name in self:
            # CABBAGE - FIGURE OUT LATER WHETHER TO ALLOW REDEFINING BY ROSTERS, OR WHETHER TO FORCE A COMMON LIVERY SET
            if livery_name in ["VANILLA", "SWOOSH", "FOO", "TGV_LA_POSTE"]:
                print(f"LiveryManager.add_livery: a roster tried to add {livery_name} when it already exists")
            else:
                raise ValueError(f"LiveryManager.add_livery: a roster tried to add {livery_name} when it already exists")
        else:
            self[livery_name] = LiveryDef(**kwargs)
        # no return as of now, not needed


class BadgeManager(list):
    """
    It's convenient to have a structure for working with badges.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_badge(self, label, **kwargs):
        # if not a duplicate, add the badge
        if self.get_badge_by_label(label) is None:
            self.append(Badge(label, **kwargs))
        # no return as of now, not needed

    def get_badge_by_label(self, label):
        for badge in self:
            if badge.label == label:
                return badge
        return None


class RailTypeManager(list):
    """
    It's convenient to have a structure for working with railtypes.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_railtypes(self, railtype_modules):
        for railtype_module_name in railtype_module_names:
            railtype_module = importlib.import_module(
                "." + railtype_module_name, package="railtypes"
            )
            railtype = railtype_module.main(disabled=False)
            self.append(railtype)

    @property
    def railtype_labels_for_railtypetable(self):
        # the railtypetable needs both lists of fallbacks by track_type_name, and all of the labels from each list so we can refer to them in e.g. tile checks
        # note that this is using the nml fallbacks for *vehicle* track_type NOT the compatible or powered powered properties for the railtypes
        # this is strictly not the scope of RailTypeManager, but it's a convenient place to add globally accessible railtype specific methods
        result = {}
        for (
            labels
        ) in global_constants.railtype_labels_by_vehicle_track_type_name.values():
            result[labels[0]] = labels
        for (
            labels
        ) in global_constants.railtype_labels_by_vehicle_track_type_name.values():
            for label in labels:
                if label not in result.keys():
                    result[label] = None
        return result


class RosterManager(list):
    """
    Sometimes we want to conveniently expose attributes that span active rosters.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as we also use it when we want a list of active rosters (the instantiated class instance behaves like a list object).
    """

    def add_rosters(self, roster_module_names):
        for roster_module_name in roster_module_names:
            roster_module = importlib.import_module(
                "." + roster_module_name, package="rosters"
            )
            roster = roster_module.main()
            self.append(roster)

        # some actions have to be run after the rosters are all added to RosterManager, to ensure all rosters are present
        for roster in self:
            for livery_name, livery_def in roster.engine_and_pax_mail_car_liveries.items():
                livery_manager.add_livery(livery_name, **livery_def)
            roster.produce_engines()
            roster.produce_wagons()
        # now validate as we have all the vehicles in all rosters
        self.validate_vehicles()
        # now complete any post validation steps
        for roster in self:
            roster.compute_wagon_recolour_sets()
            roster.add_buyable_variant_groups()

    def validate_vehicles(self):
        # has to be explicitly called after all rosters are active, and all vehicles and vehicle units are registered to each roster
        # validation will also populate numeric_id_defender which can be re-used for ID reporting
        # actual validation is delegated to the roster
        self.numeric_id_defender = {}
        for roster in self:
            roster.validate_vehicles(self.numeric_id_defender)

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
        # supports a BAD FEATURE easter egg, where some railcar speeds are increased when hauled by express engine, and can be used as fast MUs
        express_engine_ids = []
        # if we wanted cross-grf haulage bonus then this would need extending beyond active_roster; but we don't as of April 2023, so eh
        for consist in self.active_roster.engine_consists:
            # check for express-type roles, which are determined by multiple role groups
            for role in [
                "express",
                "driving_cab",
                "express_railcar",
                "high_power_railcar",
            ]:
                subroles = global_constants.role_subrole_mapping[role]
                if consist.subrole in subroles:
                    express_engine_ids.append(consist.id)
        return [(count, id) for count, id in enumerate(express_engine_ids)]

    @property
    def cargo_sprinter_ids(self):
        # find cargo_sprinters
        # used to switch wagon company colours
        result = []
        # if we wanted cross-grf cargo sprinters then this would need extending beyond active_roster; but we don't as of April 2023, so eh
        for consist in self.active_roster.engine_consists:
            # abuse the spritelayer_cargo_layers property here, we're just looking for a string, this might be fragile, but eh
            if "cargo_sprinter" in getattr(consist, "spritelayer_cargo_layers", []):
                result.append(consist.id)
        if len(result) > 255:
            raise BaseException(
                "action 2 switch is limited to 255 values, cargo_sprinter_ids exceeds this - needs split across multiple switches"
            )
        return result


def main():
    # exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
    os.makedirs(generated_files_path, exist_ok=True)

    # globals *within* this module so they can be accessed externally by other modules using iron_horse.foo
    globals()["badge_manager"] = BadgeManager()
    globals()["livery_manager"] = LiveryManager()
    globals()["railtype_manager"] = RailTypeManager()
    globals()["roster_manager"] = RosterManager()

    # railtypes
    railtype_manager.add_railtypes(railtype_module_names)

    # liveries
    for livery_name, livery_def in global_constants.freight_wagon_liveries.items():
        livery_manager.add_livery(livery_name, **livery_def)

    # rosters
    roster_manager.add_rosters(roster_module_names)

    # spritelayer cargos
    for spritelayer_cargo_module_name in spritelayer_cargo_module_names:
        spritelayer_cargo_module = importlib.import_module(
            "." + spritelayer_cargo_module_name, package="spritelayer_cargos"
        )
        spritelayer_cargo_module.main()

    # badges, done after vehicle models as badges can be either static (global), or dynamically created (for specific vehicle models)

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

    for roster in roster_manager:
        for consist in roster.consists_in_buy_menu_order:
            if consist.vehicle_family_badge is not None:
                badge_manager.add_badge(
                    label=consist.vehicle_family_badge,
                )
