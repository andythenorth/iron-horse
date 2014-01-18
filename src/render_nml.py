#!/usr/bin/env python

print "[RENDER NML] render_nml.py"

import os.path
currentdir = os.curdir
import sys
sys.path.append(os.path.join('src')) # add to the module search path

import time
from multiprocessing import Process, active_children

import codecs # used for writing files - more unicode friendly than standard open() module

import iron_horse
import utils
import global_constants

import chameleon
from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

generated_nml_path = os.path.join(iron_horse.generated_files_path, 'nml')
if not os.path.exists(generated_nml_path):
    os.mkdir(generated_nml_path)

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

def render_consist_nml(consist):
    consist_nml = codecs.open(os.path.join('generated', 'nml', consist.id + '.nml'),'w','utf8')
    consist_nml.write(utils.unescape_chameleon_output(consist.render()))
    consist_nml.close()

def main():
    consists = iron_horse.get_consists_in_buy_menu_order(show_warnings=True)

    grf_nml = codecs.open(os.path.join('iron-horse.nml'),'w','utf8')
    header_items = ['header', 'cargo_table', 'railtype_table', 'disable_default_vehicles']
    for header_item in header_items:
        template = templates[header_item + '.pynml']
        grf_nml.write(utils.unescape_chameleon_output(template(consists=consists, global_constants=global_constants,
                                                        utils=utils, sys=sys, repo_vars=repo_vars)))
 
    for consist in consists:
        Process(target=render_consist_nml, args=(consist, )).start()
    # dirty way to wait until all processes are complete before moving on
    while True:
        time.sleep(0.027) # 0.027 because it's a reference to TTD ticks :P (blame Rubidium)
        if len(active_children()) == 0:
            print "done"
            break

    for consist in consists:
        consist_nml = codecs.open(os.path.join('generated', 'nml', consist.id + '.nml'),'r','utf8').read()
        grf_nml.write(consist_nml)

    grf_nml.close()

if __name__ == '__main__': 
    main()
