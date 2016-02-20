#!/usr/bin/env python

print("[RENDER NML ONLY] render_unified_nml.py")

import codecs # used for writing files - more unicode friendly than standard open() module

import sys
import os
currentdir = os.curdir

import iron_horse
import utils
import global_constants

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates_path = os.path.join(currentdir, 'src', 'templates')
templates = PageTemplateLoader(templates_path)

consists = iron_horse.get_consists_in_buy_menu_order()

def render_header_item_nml(header_item):
    template = templates[header_item + '.pynml']

    print("Rendering " + header_item)
    return utils.unescape_chameleon_output(template(consists=consists,
                                                                   global_constants=global_constants,
                                                                   utils=utils,
                                                                   sys=sys,
                                                                   active_rosters=iron_horse.get_active_rosters(),
                                                                   repo_vars=repo_vars))

def render_consist_nml(consist):
    return utils.unescape_chameleon_output(consist.render())

def render_dispatcher(items, renderer):
    result = ''
    for item in items:
        result += renderer(item)
    return result

def main():
    rendered_nml = codecs.open(os.path.join(iron_horse.generated_files_path, 'iron-horse.nml'),'w','utf8')

    print("Rendering header items")
    header_items = ['header', 'cargo_table', 'railtype_table', 'disable_default_vehicles']
    rendered_nml.write(render_dispatcher(header_items, renderer=render_header_item_nml))

    print("Rendering consists")
    rendered_nml.write(render_dispatcher(consists, renderer=render_consist_nml))

    rendered_nml.close()

if __name__ == '__main__':
    main()
