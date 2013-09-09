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

from vehicles import chopper
from vehicles import geep
from vehicles import gridiron
from vehicles import whistler
from vehicles import zebedee
from vehicles import passenger_car
from vehicles import mail_car
from vehicles import box_car
from vehicles import tank_car
from vehicles import covered_hopper_car

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
    for vehicle in registered_vehicles:
        id = vehicle.id
        if id not in global_constants.buy_menu_sort_order:
            utils.echo_message("Warning: vehicle " + id + " in registered_vehicles, but not in buy_menu_sort_order - won't show in game")
    return sorted_vehicles

