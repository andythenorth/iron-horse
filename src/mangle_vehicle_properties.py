import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

property_to_delete = 'buy_menu_width'
property_to_move = 'sea_capable'
property_to_insert_after = 'gross_tonnage'
line_to_insert = "            property_name = 'example',"

filenames = ['screamer.py','pendolino.py','slammer.py','box_cars.py','open_cars.py','caboose_cars.py','raven.py','covered_hopper_cars.py','metro.py','gresley.py','hellenic.py','wordsell.py','goods.py','tank_cars.py','reefer_cars.py','livestock_cars.py','hopper_cars.py','flat_cars.py','passenger_cars.py','mail_cars.py','standard.py','suburban.py','collier.py','whistler.py','zebedee.py','chinook.py','gridiron.py','geep.py','dmc_sd40.py','growler.py']


def delete_property(filename):
    file = open(os.path.join('src','vehicles',filename),'r')
    content = file.readlines()

    for line in content:
        if property_to_delete in line:
            content.remove(line)

    file = open(os.path.join('src','vehicles',filename),'w')
    file.write(''.join(content))
    file.close


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
    delete_property(filename)
    #move_property(filename)
    #insert_property(filename)
