#!/usr/bin/env python

"""
  This file is part of Iron Horse Newgrf for OpenTTD.
  Iron Horse is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  Iron Horse is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with Iron Horse. If not, see <http://www.gnu.org/licenses/>.
"""
print("[RENDER DOCS] render_docs.py")

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os
currentdir = os.curdir

import time
from multiprocessing import Process, active_children

import iron_horse
import utils
import global_constants

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

docs_src = os.path.join(currentdir, 'src', 'docs_templates')
docs_output_path = os.path.join(currentdir, 'docs')
if os.path.exists(docs_output_path):
    shutil.rmtree(docs_output_path)
os.mkdir(docs_output_path)

shutil.copy(os.path.join(docs_src,'index.html'), docs_output_path)

static_dir_src = os.path.join(docs_src, 'html', 'static')
static_dir_dst = os.path.join(docs_output_path, 'html', 'static')
shutil.copytree(static_dir_src, static_dir_dst)

import markdown
from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(docs_src, format='text')

from train import Train

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()
metadata = {}
metadata['dev_thread_url'] = 'http://www.tt-forums.net/viewtopic.php?f=67&t=71219'
metadata['repo_url'] = 'http://dev.openttdcoop.org/projects/iron-horse/repository'
metadata['issue_tracker'] = 'http://dev.openttdcoop.org/projects/iron-horse/issues'

consists = iron_horse.get_consists_in_buy_menu_order()
# default sort for docs is by intro date
consists = sorted(consists, key=lambda consist: consist.intro_date)
dates = sorted([i.intro_date for i in consists])
metadata['dates'] = (dates[0], dates[-1])

class DocHelper(object):
    # dirty class to help do some doc formatting

    def get_vehicles_by_subclass(self, filter_subclasses_by_name=None):
        vehicles_by_subclass = {}
        for consist in consists:
            subclass = type(consist)
            if filter_subclasses_by_name == None or subclass.__name__ in filter_subclasses_by_name:
                if subclass in vehicles_by_subclass:
                    vehicles_by_subclass[subclass].append(consist)
                else:
                    vehicles_by_subclass[subclass] = [consist]
        return vehicles_by_subclass

    def get_engine_consists(self):
        result = []
        for i in self.get_vehicles_by_subclass(filter_subclasses_by_name='EngineConsist').values():
            result.extend(i)
        return result

    def fetch_prop(self, result, prop_name, value):
        result['vehicle'][prop_name] = value
        result['subclass_props'].append(prop_name)
        return result

    def get_props_to_print_in_code_reference(self, subclass):
        props_to_print = {}
        for vehicle in self.get_vehicles_by_subclass()[subclass]:
            result = {'vehicle':{}, 'subclass_props': []}
            result = self.fetch_prop(result, 'Vehicle Name', vehicle.get_name_substr() + base_lang_strings[vehicle.get_str_name_suffix()])
            result = self.fetch_prop(result, 'HP', int(vehicle.power))
            result = self.fetch_prop(result, 'Speed (mph)', vehicle.speed)
            result = self.fetch_prop(result, 'Weight (t)', vehicle.weight)
            result = self.fetch_prop(result, 'TE coefficient', vehicle.tractive_effort_coefficient)
            result = self.fetch_prop(result, 'Intro Date', vehicle.intro_date)
            result = self.fetch_prop(result, 'Vehicle Life', vehicle.vehicle_life)
            result = self.fetch_prop(result, 'Replacement ID', vehicle.replacement_id)
            #result = self.fetch_prop(result, 'Capacity Pax', vehicle.capacity_pax)
            #result = self.fetch_prop(result, 'Capacity Mail', vehicle.capacity_mail)
            #result = self.fetch_prop(result, 'Capacity Freight', vehicle.capacity_freight)
            result = self.fetch_prop(result, 'Buy Cost', vehicle.buy_cost)
            result = self.fetch_prop(result, 'Running Cost', vehicle.running_cost)
            #result = self.fetch_prop(result, 'Loading Speed', vehicle.loading_speed)
            #result = self.fetch_prop(result, 'Model Variants', len(vehicle.model_variants))

            props_to_print[vehicle] = result['vehicle']
            props_to_print[subclass] = result['subclass_props']

        return props_to_print

    def get_active_nav(self, doc_name, nav_link):
        return ('','active')[doc_name == nav_link]

def render_docs(doc_list, file_type, use_markdown=False):
    for doc_name in doc_list:
        template = docs_templates[doc_name + '.pt'] # .pt is the conventional extension for chameleon page templates
        doc = template(consists=consists, repo_vars=repo_vars, base_lang_strings=base_lang_strings, metadata=metadata,
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

def main():
    # render standard docs from a list
    html_docs = ['trains', 'code_reference', 'get_started', 'translations']
    txt_docs = ['license', 'readme']
    markdown_docs = ['changelog']

    render_docs(html_docs, 'html')
    render_docs(txt_docs, 'txt')
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, 'txt')
    render_docs(markdown_docs, 'html', use_markdown=True)

if __name__ == '__main__':
    main()
