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
if not os.path.exists(generated_nml_path):
    os.mkdir(generated_nml_path)

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

# we cache some nml metadata to see if we can render templated vehicles faster
nml_metadata_cache_path = os.path.join('generated', 'nml_metadata.cache')
if not os.path.exists(nml_metadata_cache_path):
    codecs.open(nml_metadata_cache_path,'w','utf8').close()
# this is fragile, playing one line python is silly :)
module_timestamps = dict((line.split('||',1)[0].strip(), line.split('||',1)[1].strip()) for line in codecs.open(nml_metadata_cache_path,'r','utf8').readlines())
nml_cache_dirty = True # !! turn off optimisation for now, needs to check for changed .py and templates files

def render_consist_nml(consist):
    # dangerous optimisation here
    if (float(module_timestamps.get(consist.vehicle_module_path, 0)) != os.stat(consist.vehicle_module_path).st_mtime) or nml_cache_dirty == True:
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

    nml_cache = codecs.open(nml_metadata_cache_path, 'w', 'utf8')

    for consist in consists:
        metadata = consist.vehicle_module_path + '||' + str(os.stat(consist.vehicle_module_path).st_mtime) + '\n'
        nml_cache.write(metadata)
        consist_nml = codecs.open(os.path.join('generated', 'nml', consist.id + '.nml'),'r','utf8').read()
        grf_nml.write(consist_nml)

    grf_nml.close()
    nml_cache.close()


if __name__ == '__main__':
    main()
