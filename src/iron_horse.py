#!/usr/bin/env python

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src'))  # add to the module search path

import global_constants
import utils
makefile_args = utils.get_makefile_args(sys)

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(
    currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

generated_files_path = os.path.join(
    currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)


# import rosters
from rosters import registered_rosters

"""
from rosters import antelope
antelope.roster.register(disabled=True)

from rosters import llama
llama.roster.register(disabled=True)
"""

from rosters import pony
pony.roster.register(disabled=False)

# import intermodal containers
import intermodal_containers

# import vehicles
from vehicles import numeric_id_defender

"""
# only comment in if needed for debugging
from vehicles import alignment_cars
alignment_cars.main()
"""

from vehicles import box_cars
box_cars.main()

from vehicles import caboose_cars
caboose_cars.main()

from vehicles import chemicals_tank_cars
chemicals_tank_cars.main()

from vehicles import coil_cars
coil_cars.main()

from vehicles import coal_hopper_cars
coal_hopper_cars.main()

from vehicles import covered_hopper_cars
covered_hopper_cars.main()

from vehicles import cryo_tank_cars
cryo_tank_cars.main()

from vehicles import curtain_side_box_cars
curtain_side_box_cars.main()

from vehicles import dump_cars
dump_cars.main()

from vehicles import dump_cars_high_side
dump_cars_high_side.main()

from vehicles import edibles_tank_cars
edibles_tank_cars.main()

from vehicles import express_cars
express_cars.main()

from vehicles import flat_cars
flat_cars.main()

from vehicles import grain_hopper_cars
grain_hopper_cars.main()

from vehicles import fruit_veg_cars
fruit_veg_cars.main()

from vehicles import hopper_cars
hopper_cars.main()

from vehicles import hst_passenger_cars
hst_passenger_cars.main()

from vehicles import intermodal_cars
intermodal_cars.main()

from vehicles import livestock_cars
livestock_cars.main()

from vehicles import luxury_passenger_cars
luxury_passenger_cars.main()

from vehicles import mail_cars
mail_cars.main()

"""
# commented out for 2.0 alpha
from vehicles import torpedo_cars
torpedo_cars.main()
"""

from vehicles import open_cars
open_cars.main()

from vehicles import passenger_cars
passenger_cars.main()

from vehicles import plate_cars
plate_cars.main()

from vehicles import reefer_cars
reefer_cars.main()

from vehicles import sliding_wall_cars
sliding_wall_cars.main()

from vehicles import stake_cars
stake_cars.main()

"""
# commented out for 2.0.x
from vehicles import silo_cars
silo_cars.main()
"""

from vehicles import tank_cars
tank_cars.main()

from vehicles import tarpaulin_cars
tarpaulin_cars.main()

"""
# commented out for 2.0.x
from vehicles import vehicle_transporter_cars
vehicle_transporter_cars.main()
"""

"""
# commented out for 2.0.x
from vehicles import well_cars
well_cars.main()
"""

def get_active_rosters():
    #  for a faster single-roster compiles when testing, optionally pass a roster id (lower case) as a makefile arg
    if makefile_args.get('roster', '*') == '*':
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
