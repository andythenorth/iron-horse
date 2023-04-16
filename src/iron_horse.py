import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

import global_constants
import utils

command_line_args = utils.get_command_line_args()

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
# exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
os.makedirs(generated_files_path, exist_ok=True)

from spritelayer_cargos import registered_spritelayer_cargos
from spritelayer_cargos import intermodal_containers
from spritelayer_cargos import automobiles

# import railtypes
from railtypes import lgv
from railtypes import lgv_electrified
from railtypes import metro
from railtypes import narrow_gauge
from railtypes import rail_electrified_ac
from railtypes import rail_electrified_ac_dc
from railtypes import rail_electrified_dc
from railtypes import rail_high_clearance

# import rosters
from rosters import ibex
from rosters import moose
from rosters import pony

# import wagons
from vehicles import acid_tank_cars
from vehicles import aggregate_cars

# from vehicles import alignment_cars
from vehicles import automobile_cars
from vehicles import bolster_cars
from vehicles import box_cars
from vehicles import bulkhead_flat_cars
from vehicles import caboose_cars
from vehicles import carbon_black_hopper_cars
from vehicles import cement_silo_cars
from vehicles import chemical_covered_hopper_cars
from vehicles import chemical_silo_cars
from vehicles import coil_buggy_cars
from vehicles import coil_cars_covered
from vehicles import coil_cars_uncovered
from vehicles import covered_hopper_cars
from vehicles import cryo_tank_cars
from vehicles import curtain_side_box_cars
from vehicles import double_deck_automobile_cars
from vehicles import dry_powder_hopper_cars
from vehicles import dump_cars
from vehicles import dump_cars_high_side
from vehicles import edibles_tank_cars
from vehicles import express_cars
from vehicles import express_intermodal_cars
from vehicles import express_railcar_passenger_trailer_cars
from vehicles import farm_products_box_cars
from vehicles import farm_products_hopper_cars
from vehicles import flat_cars
from vehicles import goods_box_cars
from vehicles import hood_open_cars
from vehicles import hopper_cars
from vehicles import hst_mail_cars
from vehicles import hst_passenger_cars
from vehicles import ingot_cars
from vehicles import intermodal_cars
from vehicles import kaolin_hopper_cars
from vehicles import livestock_cars
from vehicles import log_cars

# from vehicles import low_floor_automobile_cars
from vehicles import low_floor_intermodal_cars
from vehicles import mail_cars
from vehicles import merchandise_box_cars
from vehicles import merchandise_open_cars
from vehicles import mineral_covered_hopper_cars

# from vehicles import mineral_hopper_cars
from vehicles import mgr_hopper_cars
from vehicles import open_cars
from vehicles import ore_dump_cars
from vehicles import ore_hopper_cars
from vehicles import passenger_cars
from vehicles import peat_cars
from vehicles import plate_cars
from vehicles import pressure_tank_cars
from vehicles import product_tank_cars
from vehicles import railbus_passenger_trailer_cars
from vehicles import railcar_passenger_trailer_cars
from vehicles import randomised_box_cars
from vehicles import randomised_bulk_cars
from vehicles import randomised_chemicals_tank_cars
from vehicles import randomised_covered_hopper_cars
from vehicles import randomised_metal_coil_cars
from vehicles import randomised_dump_cars
from vehicles import randomised_flat_cars
from vehicles import randomised_hopper_cars
from vehicles import randomised_open_cars
from vehicles import randomised_piece_goods_cars
from vehicles import reefer_cars
from vehicles import restaurant_cars
from vehicles import rock_hopper_cars
from vehicles import roller_roof_hopper_cars
from vehicles import scrap_metal_cars
from vehicles import silo_cars
from vehicles import skip_cars
from vehicles import slag_ladle_cars
from vehicles import sliding_roof_cars
from vehicles import sliding_wall_cars
from vehicles import suburban_passenger_cars
from vehicles import swing_roof_hopper_cars
from vehicles import tank_cars
from vehicles import tarpaulin_cars
from vehicles import torpedo_cars
from vehicles import vehicle_parts_box_cars


class RailTypeManager(list):
    """
    It's convenient to have a structure for working with railtypes.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_railtype(self, railtype_module):
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

    def add_roster(self, roster_module):
        roster = roster_module.main()
        self.append(roster)
        # some actions have to be run after the register is added to RosterManager
        roster.post_init_actions()

    def validate_vehicles(self):
        # has to be explicitly called after all rosters are active, and all vehicles and vehicle units are registered to each roster
        # validation will also populate numeric_id_defender which can be re-used for ID reporting
        # actual validation is delegated to the roster
        self.numeric_id_defender = []
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
    def restaurant_car_ids(self):
        result = []
        print(
            "restaurant_car_ids may need to use only active roster?  Or are we allowing cross-grf restaurant cars?"
        )
        for roster in self:
            # could have abstracted the filtering element into a method on the roster, more encapsulated, but eh, code split over 2 places, so didn't
            # could also have been done by having restaurant cars register themselves directly into a list on roster but eh, that's a book-keeping headache
            for consists in roster.wagon_consists.values():
                for consist in consists:
                    if consist.__class__.__name__ == "PassengerRestaurantCarConsist":
                        result.append(consist.base_numeric_id)
        if len(result) > 255:
            utils.echo_message(
                "action 2 switch is limited to 255 values, restaurant_car_ids exceeds this - needs split across multiple switches"
            )
        return result

    @property
    def haulage_bonus_engine_id_tree(self):
        # supports a BAD FEATURE easter egg, where some railcar speeds are increased when hauled by express engine, and can be used as fast MUs
        express_engine_ids = []
        print(
            "haulage_bonus_engine_id_tree only uses active roster?  Are we allowing cross-grf haulage bonus?"
        )
        for consist in self.active_roster.engine_consists:
            # check for express-type roles, which are determined by multiple role groups
            for role_group_mapping_key in [
                "express",
                "driving_cab",
                "express_railcar",
                "high_power_railcar",
            ]:
                group_roles = global_constants.role_group_mapping[
                    role_group_mapping_key
                ]
                if consist.role in group_roles:
                    express_engine_ids.append(consist.id)
        return [(count, id) for count, id in enumerate(express_engine_ids)]

    @property
    def cargo_sprinter_ids(self):
        # find cargo_sprinters
        # used to switch wagon company colours
        result = []
        print(
            "cargo_sprinter_ids only uses active roster?  Are we allowing cross-grf cargo sprinters?"
        )
        for consist in self.active_roster.engine_consists:
            # abuse the spritelayer_cargo_layers property here, we're just looking for a string, this might be fragile, but eh
            if "cargo_sprinter" in getattr(consist, "spritelayer_cargo_layers", []):
                result.append(consist.id)
        if len(result) > 255:
            utils.echo_message(
                "action 2 switch is limited to 255 values, cargo_sprinter_ids exceeds this - needs split across multiple switches"
            )
        return result

    @property
    def pax_car_ids(self):
        # for pax cars with consist-specific liveries
        # will check for other neighbouring pax cars before showing brake car
        result = []
        print(
            "pax_car_ids only uses active roster?  Are we allowing cross-grf pax_car_ids?"
        )
        for consists in self.active_roster.wagon_consists.values():
            for consist in consists:
                if getattr(
                    consist,
                    "report_as_pax_car_to_neighbouring_vehicle_in_rulesets",
                    False,
                ):
                    result.append(consist.base_numeric_id)
        for consist in self.active_roster.engine_consists:
            if getattr(consist, "treat_as_pax_car_for_var_41", False):
                result.append(consist.id)
        if len(result) > 255:
            utils.echo_message(
                "action 2 switch is limited to 255 values, pax_car_ids result exceeds this - needs split across multiple switches"
            )
        return result


# declared outside of main, got bored trying to figure out how to otherwise put it in the module scope
railtype_manager = RailTypeManager()
roster_manager = RosterManager()


def main():
    # in the rare case that an unfinished railtype won't init cleanly, comment it out here and possibly also in the import
    # built-in support for disabled railtypes was removed as overly complex
    railtype_manager.add_railtype(lgv)
    railtype_manager.add_railtype(lgv_electrified)
    railtype_manager.add_railtype(metro)
    railtype_manager.add_railtype(narrow_gauge)
    railtype_manager.add_railtype(rail_electrified_ac)
    railtype_manager.add_railtype(rail_electrified_ac_dc)
    railtype_manager.add_railtype(rail_electrified_dc)
    railtype_manager.add_railtype(rail_high_clearance)

    # rosters
    # in the rare case that an unfinished roster won't init cleanly, comment it out here and possibly also in the import
    # built-in support for disabled rosters was removed during the conversion to multi-grf, it was an unnecessary abstraction when only one roster is used per grf
    roster_manager.add_roster(ibex)
    roster_manager.add_roster(moose)
    roster_manager.add_roster(pony)

    # spritelayer cargos
    intermodal_containers.main()
    automobiles.main()

    # wagons
    acid_tank_cars.main()
    aggregate_cars.main()
    """
    # only comment in if needed for debugging
    alignment_cars.main()
    """
    automobile_cars.main()
    bolster_cars.main()
    box_cars.main()
    bulkhead_flat_cars.main()
    caboose_cars.main()
    carbon_black_hopper_cars.main()
    cement_silo_cars.main()
    chemical_covered_hopper_cars.main()
    chemical_silo_cars.main()
    coil_buggy_cars.main()
    coil_cars_covered.main()
    coil_cars_uncovered.main()
    covered_hopper_cars.main()
    cryo_tank_cars.main()
    curtain_side_box_cars.main()
    double_deck_automobile_cars.main()
    dry_powder_hopper_cars.main()
    dump_cars.main()
    dump_cars_high_side.main()
    edibles_tank_cars.main()
    express_cars.main()
    express_intermodal_cars.main()
    express_railcar_passenger_trailer_cars.main()
    farm_products_box_cars.main()
    farm_products_hopper_cars.main()
    flat_cars.main()
    goods_box_cars.main()
    hood_open_cars.main()
    hopper_cars.main()
    hst_mail_cars.main()
    hst_passenger_cars.main()
    ingot_cars.main()
    intermodal_cars.main()
    kaolin_hopper_cars.main()
    livestock_cars.main()
    log_cars.main()
    # low_floor_automobile_cars.main()
    low_floor_intermodal_cars.main()
    mail_cars.main()
    merchandise_box_cars.main()
    merchandise_open_cars.main()
    mineral_covered_hopper_cars.main()
    # mineral_hopper_cars.main()
    mgr_hopper_cars.main()
    ore_dump_cars.main()
    ore_hopper_cars.main()
    open_cars.main()
    passenger_cars.main()
    peat_cars.main()
    plate_cars.main()
    pressure_tank_cars.main()
    product_tank_cars.main()
    reefer_cars.main()
    restaurant_cars.main()
    railbus_passenger_trailer_cars.main()
    railcar_passenger_trailer_cars.main()
    randomised_box_cars.main()
    randomised_bulk_cars.main()
    randomised_chemicals_tank_cars.main()
    randomised_covered_hopper_cars.main()
    randomised_dump_cars.main()
    randomised_flat_cars.main()
    randomised_hopper_cars.main()
    randomised_metal_coil_cars.main()
    randomised_open_cars.main()
    randomised_piece_goods_cars.main()
    rock_hopper_cars.main()
    roller_roof_hopper_cars.main()
    silo_cars.main()
    scrap_metal_cars.main()
    skip_cars.main()
    slag_ladle_cars.main()
    sliding_roof_cars.main()
    sliding_wall_cars.main()
    suburban_passenger_cars.main()
    swing_roof_hopper_cars.main()
    tank_cars.main()
    tarpaulin_cars.main()
    torpedo_cars.main()
    vehicle_parts_box_cars.main()

    roster_manager.validate_vehicles()
