#!/usr/bin/env python

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import global_constants
import utils
makefile_args = utils.get_makefile_args(sys)

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

from rosters import registered_rosters

from rosters import antelope
antelope.roster.register(disabled=True)

from rosters import llama
llama.roster.register(disabled=True)

from rosters import pony
pony.roster.register(disabled=False)

from vehicles import box_cars
box_cars.main()

from vehicles import caboose_cars
caboose_cars.main()

from vehicles import covered_hopper_cars
covered_hopper_cars.main()

from vehicles import edibles_tank_cars
edibles_tank_cars.main()

from vehicles import flat_cars
flat_cars.main()

from vehicles import fruit_cars
fruit_cars.main()

from vehicles import hopper_cars
hopper_cars.main()

from vehicles import intermodal_flat_cars
intermodal_flat_cars.main()

from vehicles import livestock_cars
livestock_cars.main()

from vehicles import mail_box_cars
mail_box_cars.main()

from vehicles import mail_cars
mail_cars.main()

from vehicles import metal_cars
metal_cars.main()

from vehicles import open_cars
open_cars.main()

from vehicles import passenger_cars
passenger_cars.main()

from vehicles import reefer_cars
reefer_cars.main()

from vehicles import special_passenger_cars
special_passenger_cars.main()

from vehicles import supplies_cars
supplies_cars.main()

from vehicles import tank_cars
tank_cars.main()

from vehicles import vehicle_transporter_cars
vehicle_transporter_cars.main()


def get_active_rosters():
    #  for a faster single-roster compiles when testing, optionally pass a roster id (lower case) as a makefile arg
    if makefile_args.get('roster', '*') == '*':
        active_rosters = [roster for roster in registered_rosters if not roster.disabled]
    else:
        active_rosters = [roster for roster in registered_rosters if roster.id == makefile_args['roster']] # make sure it's iterable
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
        utils.echo_message("Warning: consist " + id + " in buy_menu_sort_order, but not found in registered_consists")
    for id in consist_id_defender.difference(buy_menu_defender):
        utils.echo_message("Warning: consist " + id + " in consists, but not in buy_menu_sort_order - won't show in game")
    # when adding vehicles it's useful to know what the next free numeric ID is
    numeric_ids = sorted([consist.base_numeric_id for consist in consists])
    # tidy-mind problem, but do we have any vacant numeric ID slots in the currently used range?
    # 'print' eh? - but it's fine echo_message isn't intended for this kind of info, don't bother changing
    print("Vacant numeric ID slots:", ', '.join([str(i) for i in numeric_ids if not (i - 10) in numeric_ids and i is not 0]), "anything >", max(numeric_ids))

    return consists


