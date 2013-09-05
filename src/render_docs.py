#!/usr/bin/env python

"""
  This file is part of FISH Newgrf for OpenTTD.
  FISH is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FISH is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FISH. If not, see <http://www.gnu.org/licenses/>.
"""
print "[PYTHON] render docs"

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import global_constants
import os
currentdir = os.curdir

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

docs_src = os.path.join(currentdir, 'docs_src')
docs_output_path = os.path.join(currentdir, 'docs')
if os.path.exists(docs_output_path):
    shutil.rmtree(docs_output_path)
os.mkdir(docs_output_path)

shutil.copy(os.path.join(docs_src,'index.html'), docs_output_path)

static_dir_src = os.path.join(currentdir, 'docs_src', 'html', 'static')
static_dir_dst = os.path.join(docs_output_path, 'html', 'static')
shutil.copytree(static_dir_src, static_dir_dst)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(os.path.join(currentdir, 'docs_src'), format='text')

import utils as utils
import markdown

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()

import fish
from ship import Ship, Trawler, MixinRefittableCapacity

ships = fish.get_ships_in_buy_menu_order()
# default sort for docs is by ship intro date
ships = sorted(ships, key=lambda ship: ship.intro_date)

metadata = {}
dates = sorted([i.intro_date for i in ships])
metadata['dates'] = (dates[0], dates[-1])
metadata['dev_thread_url'] = 'http://www.tt-forums.net/viewtopic.php?f=26&t=44613'
metadata['repo_url'] = 'http://dev.openttdcoop.org/projects/fish/repository'
metadata['issue_tracker'] = 'http://dev.openttdcoop.org/projects/fish/issues'

class DocHelper(object):
    # dirty class to help do some doc formatting

    def get_ships_by_subclass(self):
        ships_by_subclass = {}
        for ship in ships:
            subclass = type(ship)
            if subclass in ships_by_subclass:
                ships_by_subclass[subclass].append(ship)
            else:
                ships_by_subclass[subclass] = [ship]
        return ships_by_subclass

    def fetch_prop(self, result, prop_name, value):
        result['ship'][prop_name] = value
        result['subclass_props'].append(prop_name)
        return result

    def get_props_to_print_in_code_reference(self, subclass):
        props_to_print = {}
        for ship in self.get_ships_by_subclass()[subclass]:
            result = {'ship':{}, 'subclass_props': []}

            result = self.fetch_prop(result, 'Ship Name', ship.get_name_substr() + base_lang_strings[ship.get_str_name_suffix()])
            result = self.fetch_prop(result, 'Extra Info', base_lang_strings[ship.get_str_type_info()])
            result = self.fetch_prop(result, 'Speed Laden', int(ship.speed))
            result = self.fetch_prop(result, 'Speed Unladen', int(ship.speed_unladen))
            result = self.fetch_prop(result, 'Canal Speed Fraction', ship.canal_speed)
            result = self.fetch_prop(result, 'Ocean Speed Fraction', ship.ocean_speed)
            result = self.fetch_prop(result, 'Intro Date', ship.intro_date)
            result = self.fetch_prop(result, 'Vehicle Life', ship.vehicle_life)
            result = self.fetch_prop(result, 'Replacement ID', ship.replacement_id)
            result = self.fetch_prop(result, 'Capacity Pax', ship.capacity_pax)
            result = self.fetch_prop(result, 'Capacity Mail', ship.capacity_mail)
            result = self.fetch_prop(result, 'Capacity Freight', ship.capacity_freight)
            if isinstance(ship, Trawler):
                result = self.fetch_prop(result, 'Capacity Fish Holds', ship.capacity_fish_holds)
            if isinstance(ship, MixinRefittableCapacity):
                result = self.fetch_prop(result, 'Capacities Refittable', ', '.join(str(i) for i in ship.capacities_refittable))
            result = self.fetch_prop(result, 'Gross Tonnage', ship.gross_tonnage)
            result = self.fetch_prop(result, 'Buy Cost', ship.buy_cost)
            result = self.fetch_prop(result, 'Running Cost', ship.running_cost)
            result = self.fetch_prop(result, 'Loading Speed', ship.loading_speed)
            result = self.fetch_prop(result, 'Model Variants', len(ship.model_variants))
            result = self.fetch_prop(result, 'Graphics Status', ship.graphics_status)

            props_to_print[ship] = result['ship']
            props_to_print[subclass] = result['subclass_props']

        return props_to_print

    def get_active_nav(self, doc_name, nav_link):
        return ('','active')[doc_name == nav_link]

def render_docs(doc_list, file_type, use_markdown=False):
    for doc_name in doc_list:
        template = docs_templates[doc_name + '.pt'] # .pt is the conventional extension for chameleon page templates
        doc = template(ships=ships, repo_vars=repo_vars, base_lang_strings=base_lang_strings, metadata=metadata,
                       utils=utils, doc_helper=DocHelper(), doc_name=doc_name)
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = docs_templates['markdown_wrapper.pt']
            doc = markdown_wrapper(content=markdown.markdown(doc), global_constants=global_constants, repo_vars=repo_vars,
                              metadata=metadata, utils=utils, doc_helper=DocHelper(), doc_name=doc_name)
        if file_type == 'html':
            subdir = 'html'
        else:
            subdir = ''
        # save the results of templating
        doc_file = codecs.open(os.path.join(docs_output_path, subdir, doc_name + '.' + file_type), 'w','utf8')
        doc_file.write(doc)
        doc_file.close()


# render standard docs from a list
html_docs = ['ships', 'code_reference', 'get_started', 'translations']
txt_docs = ['license', 'readme']
markdown_docs = ['changelog']

render_docs(html_docs, 'html')
render_docs(txt_docs, 'txt')
# just render the markdown docs twice to get txt and html versions, simples no?
render_docs(markdown_docs, 'txt')
render_docs(markdown_docs, 'html', use_markdown=True)
