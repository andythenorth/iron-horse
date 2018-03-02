from time import time

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os
currentdir = os.curdir
from time import time

from PIL import Image

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

# we'll be processing some extra images and saving them into the img dir
images_dir_dst = os.path.join(static_dir_dst, 'img')

import markdown
from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(docs_src, format='text')

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

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

registered_rosters = iron_horse.registered_rosters

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
            result = self.fetch_prop(result, 'Buy Cost', vehicle.buy_cost)
            result = self.fetch_prop(result, 'Running Cost', vehicle.running_cost)
            #result = self.fetch_prop(result, 'Loading Speed', vehicle.loading_speed)
            #result = self.fetch_prop(result, 'Model Variants', len(vehicle.model_variants))

            props_to_print[vehicle] = result['vehicle']
            props_to_print[subclass] = result['subclass_props']

        return props_to_print

    def get_base_numeric_id(self, consist):
        return consist.base_numeric_id

    def get_active_nav(self, doc_name, nav_link):
        return ('','active')[doc_name == nav_link]

def render_docs(doc_list, file_type, use_markdown=False):
    for doc_name in doc_list:
        template = docs_templates[doc_name + '.pt'] # .pt is the conventional extension for chameleon page templates
        doc = template(consists=consists, global_constants=global_constants, registered_rosters=registered_rosters, makefile_args=makefile_args,
                       base_lang_strings=base_lang_strings, metadata=metadata, utils=utils, doc_helper=DocHelper(), doc_name=doc_name)
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = docs_templates['markdown_wrapper.pt']
            doc = markdown_wrapper(content=markdown.markdown(doc), global_constants=global_constants, makefile_args=makefile_args,
                              metadata=metadata, utils=utils, doc_helper=DocHelper(), doc_name=doc_name)
        if file_type == 'html':
            subdir = 'html'
        else:
            subdir = ''
        # save the results of templating
        doc_file = codecs.open(os.path.join(docs_output_path, subdir, doc_name + '.' + file_type), 'w','utf8')
        doc_file.write(doc)
        doc_file.close()

def render_docs_images():
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs
    vehicle_graphics_src = os.path.join(currentdir, 'generated', 'graphics')
    for consist in consists:
        vehicle_spritesheet = Image.open(os.path.join(vehicle_graphics_src, consist.id + '_0.png'))
        # !! currently assumes buy menu sprite in 7th column, this won't always be valid assumption, and needs to be detected in the vehicle (which knows)
        processed_vehicle_image = vehicle_spritesheet.crop(box=(consist.buy_menu_x_loc,
                                                                10,
                                                                consist.buy_menu_x_loc + global_constants.buy_menu_sprite_width,
                                                                10 + global_constants.buy_menu_sprite_height))
        # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
        processed_vehicle_image = processed_vehicle_image.resize((4 * global_constants.buy_menu_sprite_width, 4 * global_constants.buy_menu_sprite_height),
                                                                  resample=Image.NEAREST)
        output_path = os.path.join(images_dir_dst, consist.id + '.png')
        processed_vehicle_image.save(output_path, optimize=True, transparency=0)

def main():
    start = time()
    print("[RENDER DOCS] render_docs.py")

    # render standard docs from a list
    html_docs = ['trains', 'code_reference', 'get_started', 'translations']
    txt_docs = ['license', 'readme']
    markdown_docs = ['changelog']

    render_docs(html_docs, 'html')
    render_docs(txt_docs, 'txt')
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, 'txt')
    render_docs(markdown_docs, 'html', use_markdown=True)
    # process images for use in docs
    render_docs_images()

    print(format((time() - start), '.2f')+'s')

if __name__ == '__main__':
    main()
