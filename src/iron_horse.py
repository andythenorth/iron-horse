#!/usr/bin/env python

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import global_constants
import utils

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path


# get args passed by makefile
if len(sys.argv) > 1:
    repo_vars = {'repo_title' : sys.argv[1], 'repo_version' : sys.argv[2]}
else: # provide some defaults so templates don't explode when testing python script without command line args
    repo_vars = {'repo_title' : 'FISH - compiled without makefile', 'repo_version' : 1}

print "[IMPORT VEHICLES] iron_horse.py"

import train
from train import Train
from vehicles import registered_vehicles

from vehicles import box_cars
from vehicles import chopper
from vehicles import covered_hopper_cars
#from vehicles import dmc_sd40
#from vehicles import geep
from vehicles import gridiron
from vehicles import hopper_cars
from vehicles import livestock_cars
from vehicles import mail_cars
from vehicles import open_cars
from vehicles import passenger_cars
from vehicles import raven
from vehicles import reefer_cars
from vehicles import suburban
from vehicles import tank_cars
from vehicles import whistler
from vehicles import zebedee

def get_vehicles_in_buy_menu_order():
    sorted_vehicles = []
    # first compose the buy menu order list
    buy_menu_sort_order = list(global_constants.buy_menu_sort_order_locos) # copy the list in global_constants to avoid unwanted modifications to it
    for id_base in global_constants.buy_menu_sort_order_wagons:
        for vehicle_set in global_constants.vehicle_set_id_mapping.keys():
            for wagon_generation in range(1, global_constants.num_wagon_generations + 1):
                wagon_id = '_'.join((id_base, vehicle_set, 'gen', str(wagon_generation)))
                buy_menu_sort_order.append(wagon_id)

    # now check registered vehicles against the buy menu order, and add them to the sorted list
    for id in buy_menu_sort_order:
        found = False
        for vehicle in registered_vehicles:
            if vehicle.id == id:
                sorted_vehicles.append(vehicle)
                found = True
        if not found:
            utils.echo_message("Warning: vehicle " + id + " in buy_menu_sort_order, but not found in registered_vehicles")

    # now guard against any vehicles missing from buy menu order, as that wastes time asking 'wtf?' when they don't appear in game
    for vehicle in registered_vehicles:
        id = vehicle.id
        if id not in buy_menu_sort_order:
            utils.echo_message("Warning: vehicle " + id + " in registered_vehicles, but not in buy_menu_sort_order - won't show in game")
    return sorted_vehicles

