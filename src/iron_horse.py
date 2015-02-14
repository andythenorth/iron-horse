#!/usr/bin/env python

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import global_constants
import utils
import graphics_processor.pipelines

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

# get args passed by makefile
if len(sys.argv) > 1:
    repo_vars = {'repo_title' : sys.argv[1], 'repo_version' : sys.argv[2]}
else: # provide some defaults so templates don't explode when testing python script without command line args
    repo_vars = {'repo_title' : 'FISH - compiled without makefile', 'repo_version' : 1}

print("[IMPORT VEHICLES] iron_horse.py")

from vehicles import registered_consists, registered_wagon_generations

from vehicles import box_cars
box_cars.main()

from vehicles import caboose_cars
caboose_cars.main()

from vehicles import combine_cars
combine_cars.main()

from vehicles import covered_hopper_cars
covered_hopper_cars.main()

from vehicles import edibles_tank_cars
edibles_tank_cars.main()

from vehicles import flat_cars
flat_cars.main()

from vehicles import hopper_cars
hopper_cars.main()

from vehicles import intermodal_flat_cars
intermodal_flat_cars.main()

from vehicles import livestock_cars
livestock_cars.main()

from vehicles import mail_cars
mail_cars.main()

from vehicles import metal_cars
metal_cars.main()

from vehicles import metro_cars
metro_cars.main()

from vehicles import open_cars
open_cars.main()

from vehicles import passenger_cars
passenger_cars.main()

from vehicles import reefer_cars
reefer_cars.main()

from vehicles import supplies_cars
supplies_cars.main()

from vehicles import tank_cars
tank_cars.main()

from rosters import registered_rosters

from rosters import brit
brit.roster.register()

from rosters import soam
soam.roster.register()

def get_consists_in_buy_menu_order(show_warnings=False):
    sorted_consists = []
    # first compose the buy menu order list
    buy_menu_sort_order = []
    # first compose the buy menu order list
    for roster in registered_rosters:
        buy_menu_sort_order.extend(roster.buy_menu_sort_order)

    for id_base in global_constants.buy_menu_sort_order_wagons:
        for vehicle_set in global_constants.vehicle_set_id_mapping.keys():
            for wagon_generation in registered_wagon_generations[vehicle_set].get(id_base, []):
                wagon_id = '_'.join((id_base, vehicle_set, 'gen', str(wagon_generation)))
                buy_menu_sort_order.append(wagon_id)

    # now check registered vehicles against the buy menu order, and add them to the sorted list
    for id in buy_menu_sort_order:
        found = False
        for consist in registered_consists:
            if consist.id == id:
                sorted_consists.append(consist)
                found = True
        if show_warnings and not found:
            utils.echo_message("Warning: consist " + id + " in buy_menu_sort_order, but not found in registered_consists")

    # now guard against any consists missing from buy menu order, as that wastes time asking 'wtf?' when they don't appear in game
    for consist in registered_consists:
        id = consist.id
        if show_warnings and id not in buy_menu_sort_order:
            utils.echo_message("Warning: consist " + id + " in registered_consists, but not in buy_menu_sort_order - won't show in game")
    return sorted_consists


