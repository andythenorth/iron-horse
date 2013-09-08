import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

property_to_move = 'sea_capable'
property_to_insert_after = 'gross_tonnage'
line_to_insert = "            graphics_status = 'Unstarted',"

filenames = ['altamira_freighter.py',]


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
