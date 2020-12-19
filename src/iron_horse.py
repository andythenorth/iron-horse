import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src'))  # add to the module search path

import global_constants
import utils
makefile_args = utils.get_makefile_args(sys)

generated_files_path = os.path.join(
    currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

# import rosters
from rosters import registered_rosters
from rosters import pony

from vehicles import numeric_id_defender

# this format of import is weird, but I don't want the imported modules directly in the iron horse namespace, I want to nest in spritelayer_cargos
import spritelayer_cargos.intermodal_containers
import spritelayer_cargos.vehicles_cargos

# import wagons
#from vehicles import alignment_cars
from vehicles import bolster_cars
from vehicles import box_cars
from vehicles import bulkhead_flat_cars
from vehicles import caboose_cars
from vehicles import carbon_black_hopper_cars
from vehicles import cement_silo_cars
from vehicles import coil_buggy_cars
from vehicles import coil_cars_covered
from vehicles import coil_cars_uncovered
from vehicles import covered_hopper_cars
from vehicles import cryo_tank_cars
from vehicles import curtain_side_box_cars
from vehicles import dump_cars
from vehicles import dump_cars_high_side
from vehicles import edibles_tank_cars
from vehicles import express_cars
from vehicles import express_intermodal_cars
from vehicles import flat_cars
from vehicles import fruit_veg_cars
from vehicles import grain_hopper_cars
from vehicles import hopper_cars
from vehicles import hst_passenger_cars
from vehicles import ingot_cars
from vehicles import intermodal_cars
from vehicles import livestock_cars
from vehicles import log_cars
from vehicles import low_floor_intermodal_cars
from vehicles import luxury_passenger_cars
from vehicles import mail_cars
from vehicles import torpedo_cars
from vehicles import open_cars
from vehicles import ore_hopper_cars
from vehicles import passenger_cars
from vehicles import pellet_hopper_cars
from vehicles import plate_cars
from vehicles import product_tank_cars
from vehicles import railcar_luxury_passenger_trailer_cars
from vehicles import railcar_passenger_trailer_cars
from vehicles import reefer_cars
from vehicles import rock_hopper_cars
from vehicles import scrap_metal_cars
from vehicles import silo_cars
from vehicles import slag_ladle_cars
from vehicles import sliding_roof_cars
from vehicles import sliding_wall_cars
from vehicles import tank_cars
from vehicles import tarpaulin_cars
from vehicles import vehicle_parts_box_cars
from vehicles import vehicle_transporter_cars

def get_active_rosters():
    #  for a faster single-roster compiles when testing, optionally pass a roster id (lower case) as a makefile arg
    if makefile_args.get('roster', 'ALL') == 'ALL':
        active_rosters = [
            roster for roster in registered_rosters if not roster.disabled]
    else:
        active_rosters = [roster for roster in registered_rosters if roster.id ==
                          makefile_args['roster']]  # make sure it's iterable
    return active_rosters


def get_consists_in_buy_menu_order():
    consists = []
    # first compose the buy menu order list
    buy_menu_sort_order = []
    active_rosters = get_active_rosters()
    for roster in active_rosters:
        buy_menu_sort_order.extend(roster.buy_menu_sort_order)
        consists.extend(roster.consists_in_buy_menu_order)

    # now guard against any consists missing from buy menu order or vice versa, as that wastes time asking 'wtf?' when they don't appear in game
    consist_id_defender = set([consist.id for consist in consists])
    buy_menu_defender = set(buy_menu_sort_order)
    for id in buy_menu_defender.difference(consist_id_defender):
        utils.echo_message("Warning: consist " + id +
                           " in buy_menu_sort_order, but not found in registered_consists")
    for id in consist_id_defender.difference(buy_menu_defender):
        utils.echo_message("Warning: consist " + id +
                           " in consists, but not in buy_menu_sort_order - won't show in game")
    return consists


def vacant_numeric_ids_formatted():
    # when adding vehicles it's useful to know what the next free numeric ID is
    # tidy-mind problem, but do we have any vacant numeric ID slots in the currently used range?
    # 'print' eh? - but it's fine echo_message isn't intended for this kind of info, don't bother changing
    max_id = max(numeric_id_defender) -  (max(numeric_id_defender) % 10)
    id_gaps = []
    for i in range(0, int(max_id/10)):
        id = i * 10
        if id not in numeric_id_defender:
            id_gaps.append(str(id))
    return "Vacant numeric ID slots: " + ', '.join(id_gaps) + (" and from " if len(id_gaps) > 0 else '') + str(max_id + 10) + " onwards"

def get_haulage_bonus_engine_id_tree():
    # supports a BAD FEATURE easter egg, where some railcar speeds are increased when hauled by express engine, and can be used as fast MUs
    express_engine_ids = []
    for roster in get_active_rosters():
        for consist in roster.engine_consists:
            # check for express-type roles, which are determined by multiple role groups
            for role_group_mapping_key in ['express', 'driving_cab', 'luxury_railcar']:
                group_roles = global_constants.role_group_mapping[role_group_mapping_key]
                if consist.role in group_roles:
                    express_engine_ids.append(consist.id)
    return [(count, id) for count, id in enumerate(express_engine_ids)]

def get_livery_2_engine_ids():
    # for vehicles with consist-specific liveries
    # will switch vehicle to livery 2 for specific roles of lead engine
    result = []
    for roster in get_active_rosters():
        for consist in roster.engine_consists:
            # second livery choice is deliberate, means 'as seen in buy menu' livery is built for common case of express 1, heavy_express 1
            # note that -2 is used for heavy_express, be careful which engines are in this joker branch
            # ! this (x,y) tuple format is weird and won't scale well, see train.py intro_date_days_offset() for a dict based solution to a similar problem
            if (consist.role, consist.role_child_branch_num) in [('branch_express', 1), ('express', 2), ('heavy_express', 2), ('heavy_express', -2), ('pax_railcar', 2), ('mail_railcar', 2)]:
                result.append(consist.id)
    if len(result) > 255:
        utils.echo_message("action 2 switch is limited to 255 values, get_livery_2_engine_ids exceeds this - needs split across multiple switches")
    return result

def get_pax_car_ids():
    # for pax cars with consist-specific liveries
    # will check for other neighbouring pax cars before showing brake car
    result = []
    for roster in get_active_rosters():
        for consists in roster.wagon_consists.values():
            for consist in consists:
                if getattr(consist, 'report_as_pax_car_to_neighbouring_vehicle_in_rulesets', False):
                    result.append(consist.base_numeric_id)
    if len(result) > 255:
        utils.echo_message("action 2 switch is limited to 255 values, get_pax_car_ids exceeds this - needs split across multiple switches")
    return result

def main():
    # rosters
    pony.main(disabled=False)

    # cargos that use spritelayers (most dont')
    spritelayer_cargos.intermodal_containers.main()
    spritelayer_cargos.vehicles_cargos.main()

    # wagons
    """
    # only comment in if needed for debugging
    alignment_cars.main()
    """
    bolster_cars.main()
    box_cars.main()
    bulkhead_flat_cars.main()
    caboose_cars.main()
    carbon_black_hopper_cars.main()
    cement_silo_cars.main()
    coil_buggy_cars.main()
    coil_cars_covered.main()
    coil_cars_uncovered.main()
    covered_hopper_cars.main()
    cryo_tank_cars.main()
    curtain_side_box_cars.main()
    dump_cars.main()
    dump_cars_high_side.main()
    edibles_tank_cars.main()
    express_cars.main()
    express_intermodal_cars.main()
    flat_cars.main()
    fruit_veg_cars.main()
    grain_hopper_cars.main()
    hopper_cars.main()
    hst_passenger_cars.main()
    ingot_cars.main()
    intermodal_cars.main()
    livestock_cars.main()
    log_cars.main()
    low_floor_intermodal_cars.main()
    luxury_passenger_cars.main()
    mail_cars.main()
    ore_hopper_cars.main()
    open_cars.main()
    passenger_cars.main()
    pellet_hopper_cars.main()
    plate_cars.main()
    product_tank_cars.main()
    reefer_cars.main()
    railcar_luxury_passenger_trailer_cars.main()
    railcar_passenger_trailer_cars.main()
    rock_hopper_cars.main()
    silo_cars.main()
    scrap_metal_cars.main()
    slag_ladle_cars.main()
    sliding_roof_cars.main()
    sliding_wall_cars.main()
    tank_cars.main()
    tarpaulin_cars.main()
    torpedo_cars.main()
    vehicle_parts_box_cars.main()
    vehicle_transporter_cars.main()
