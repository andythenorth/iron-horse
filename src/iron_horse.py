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

# import intermodal containers
import intermodal_containers

# import wagons
#from vehicles import alignment_cars
from vehicles import box_cars
from vehicles import caboose_cars
from vehicles import carbon_black_hopper_cars
from vehicles import chemicals_tank_cars
from vehicles import coil_cars
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
from vehicles import intermodal_cars
from vehicles import livestock_cars
from vehicles import luxury_passenger_cars
from vehicles import mail_cars
from vehicles import torpedo_cars
from vehicles import open_cars
from vehicles import ore_hopper_cars
from vehicles import minerals_covered_hopper_cars
from vehicles import passenger_cars
# from vehicles import petrol_tank_cars # unconvinced so far
from vehicles import plate_cars
from vehicles import reefer_cars
from vehicles import rock_hopper_cars
from vehicles import rubber_tank_cars
from vehicles import sulphur_tank_cars
from vehicles import scrap_metal_cars
from vehicles import sliding_wall_cars
from vehicles import stake_cars
from vehicles import silo_cars
from vehicles import slag_ladle_cars
from vehicles import tank_cars
from vehicles import tarpaulin_cars
#from vehicles import vehicle_transporter_cars
#from vehicles import well_cars

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
            if consist.role in global_constants.role_group_mapping['express'] or consist.role in global_constants.role_group_mapping['driving_cab']:
                express_engine_ids.append(consist.id)
    return [(count, id) for count, id in enumerate(express_engine_ids)]

def get_livery_2_engine_ids():
    # for vehicles with consist-specific liveries
    # will switch vehicle to livery 2 for specific roles of lead engine
    result = []
    for roster in get_active_rosters():
        for consist in roster.engine_consists:
            # second livery choice is deliberate, means 'as seen in buy menu' livery is built for common case of express_1, heavy_express_1
            # 'heavy_express_4' doesn't use livery_2 by design (tied to Pony engine livery assumptions)
            if consist.role in ['branch_express_1', 'branch_express_2', 'express_2', 'heavy_express_2', 'pax_railcar_2', 'mail_railcar_2']:
                result.append(consist.id)
    return result

def main():
    pony.main(disabled=False)
    intermodal_containers.main()
    # wagons
    """
    # only comment in if needed for debugging
    alignment_cars.main()
    """
    box_cars.main()
    caboose_cars.main()
    carbon_black_hopper_cars.main()
    chemicals_tank_cars.main()
    coil_cars.main()
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
    intermodal_cars.main()
    livestock_cars.main()
    luxury_passenger_cars.main()
    mail_cars.main()
    minerals_covered_hopper_cars.main()
    ore_hopper_cars.main()
    open_cars.main()
    passenger_cars.main()
    # petrol_tank_cars.main() # unconvinced so far
    plate_cars.main()
    reefer_cars.main()
    rock_hopper_cars.main()
    rubber_tank_cars.main() # unconvinced so far
    silo_cars.main()
    scrap_metal_cars.main()
    slag_ladle_cars.main()
    sliding_wall_cars.main()
    stake_cars.main()
    sulphur_tank_cars.main() # unconvinced so far
    tank_cars.main()
    tarpaulin_cars.main()
    torpedo_cars.main()
    """
    # commented out for 2.x
    from vehicles import vehicle_transporter_cars
    vehicle_transporter_cars.main()
    """
    """
    # commented out for 2.x
    from vehicles import well_cars
    well_cars.main()
    """
