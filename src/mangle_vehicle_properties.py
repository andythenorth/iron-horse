import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

property_to_move = 'sea_capable'
property_to_insert_after = 'gross_tonnage'
line_to_insert = "            graphics_status = 'Unstarted',"

filenames = ['altamira_freighter.py',
         'barletta_paddle_steamer.py',
         'cape_spear_trawler.py',
         'capo_sandalo_vehicle_ferry.py',
         'castle_point_steamer.py',
         'eddystone_tanker.py',
         'endeavour_utility_catamaran.py',
         'enoshima_catamaran_ferry.py',
         'fastnet_paddle_steamer.py',
         'feodosiya_hydrofoil.py',
         'fish_island_trawler.py',
         'frisco_bay_freighter.py',
         'harbour_point_utility_vessel.py',
         'hopetown_tanker.py',
         'lindau_freight_barge.py',
         'little_cumbrae_freighter.py',
         'marstein_freighter.py',
         'maspalomas_freighter.py',
         'matsushima_hydrofoil.py',
         'mount_blaze_catamaran_ferry.py',
         'nieuwpoort_container_feeder.py',
         'patos_island_vehicle_ferry.py',
         'pine_island_log_tug.py',
         'saint_marie_barge_tug.py',
         'santorini_freighter.py',
         'shark_island_livestock_ship.py',
         'sunk_rock_ferry.py',
         'thunder_bay_hovercraft.py',
         'whitgift_freight_barge.py',
         'yokohama_tanker.py']


def move_property(filename):
    file = open(os.path.join('src','vehicles',filename),'r')
    content = file.readlines()

    for line in content:
        if property_to_move in line:
            cut_line = line
    content.remove(cut_line)
    for line in content:
        if property_to_insert_after in line:
            line_to_insert_after = line
    insert_position = content.index(line_to_insert_after)
    content.insert(insert_position+1, cut_line)
    #print ''.join(content)

    file = open(os.path.join('src','vehicles',filename),'w')
    file.write(''.join(content))
    file.close

def insert_property(filename):
    file = open(os.path.join('src','vehicles',filename),'r')
    content = file.readlines()

    for line in content:
        if property_to_insert_after in line:
            line_to_insert_after = line
    insert_position = content.index(line_to_insert_after)
    content.insert(insert_position+1, line_to_insert)
    #print ''.join(content)

    file = open(os.path.join('src','vehicles',filename),'w')
    file.write(''.join(content))
    file.close


for filename in filenames:
    #move_property(filename)
    insert_property(filename)
