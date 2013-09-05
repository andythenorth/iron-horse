print "[RENDER NML] render_nml.py"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

import fish
import utils
import global_constants

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

ships = fish.get_ships_in_buy_menu_order()

grf_nml = codecs.open(os.path.join('iron-horse.nml'),'w','utf8')
header_items = ['header', 'cargo_table', 'disable_default_ships']
for header_item in header_items:
    template = templates[header_item + '.pynml']
    templated_nml = utils.unescape_chameleon_output(template(ships=ships, global_constants=global_constants,
                                                    utils=utils, sys=sys, repo_vars=repo_vars))
    # append the results of templating
    grf_nml.write(templated_nml)

for ship in ships:
    templated_nml = ship.render()
    # an ugly hack here because chameleon html escapes some characters
    templated_nml = '>'.join(templated_nml.split('&gt;'))
    templated_nml = '&'.join(templated_nml.split('&amp;'))
    grf_nml.write(templated_nml)

grf_nml.close()
