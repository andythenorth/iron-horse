#!/usr/bin/env python

print "[RENDER NML] render_nml.py"

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os
currentdir = os.curdir
from multiprocessing import Pool

import iron_horse
import utils
import global_constants

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

generated_nml_path = os.path.join(iron_horse.generated_files_path, 'nml')
if os.path.exists(generated_nml_path):
    shutil.rmtree(generated_nml_path)
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
 
    pool = Pool(processes=16) # 16 is an arbitrary amount that appears to be fast without blocking the system  
    pool.map(render_consist_nml, consists)
    pool.close()
    pool.join()

    for consist in consists:
        consist_nml = codecs.open(os.path.join('generated', 'nml', consist.id + '.nml'),'r','utf8').read()
        grf_nml.write(consist_nml)

    grf_nml.close()

if __name__ == '__main__': 
    main()
