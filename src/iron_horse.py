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

import ship
from ship import Ship
from vehicles import registered_vehicles

from vehicles import altamira_freighter
from vehicles import cape_spear_trawler
from vehicles import capo_sandalo_vehicle_ferry
from vehicles import castle_point_steamer
from vehicles import eddystone_tanker


def get_vehicles_in_buy_menu_order():
    sorted_vehicles = []
    for id in global_constants.buy_menu_sort_order:
        found = False
        for vehicle in registered_vehicles:
            if vehicle.id == id:
                sorted_vehicles.append(vehicle)
                found = True
        if not found:
            utils.echo_message("Warning: vehicle " + id + " in buy_menu_sort_order, but not found in registered_vehicles")
    return sorted_vehicles

