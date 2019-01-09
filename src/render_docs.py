print("[RENDER DOCS] render_docs.py")

import codecs  # used for writing files - more unicode friendly than standard open() module

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
chameleon_cache_path = os.path.join(
    currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

docs_src = os.path.join(currentdir, 'src', 'docs_templates')
docs_output_path = os.path.join(currentdir, 'docs')
if os.path.exists(docs_output_path):
    shutil.rmtree(docs_output_path)
os.mkdir(docs_output_path)

shutil.copy(os.path.join(docs_src, 'index.html'), docs_output_path)

static_dir_src = os.path.join(docs_src, 'html', 'static')
static_dir_dst = os.path.join(docs_output_path, 'html', 'static')
shutil.copytree(static_dir_src, static_dir_dst)

# we'll be processing some extra images and saving them into the img dir
images_dir_dst = os.path.join(static_dir_dst, 'img')

import markdown
# chameleon used in most template cases
from chameleon import PageTemplateLoader
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

    # Some constants

    # these only used in docs as of April 2018
    buy_menu_sprite_max_width = 65 # up to 2 units eh
    buy_menu_sprite_height = 16

    def buy_menu_sprite_width(self, consist):
        if not consist.dual_headed:
            return min((4 * consist.length) + 1, self.buy_menu_sprite_max_width)
        # openttd automatically handles dual head, but we need to calculate double width explicitly for docs
        if consist.dual_headed:
            return min((2 * 4 * consist.length) + 1, self.buy_menu_sprite_max_width)

    def get_vehicles_by_subclass(self, filter_subclasses_by_name=None):
        # first find all the subclasses + their vehicles
        vehicles_by_subclass = {}
        for consist in consists:
            subclass = type(consist)
            if filter_subclasses_by_name == None or subclass.__name__ in filter_subclasses_by_name:
                if subclass in vehicles_by_subclass:
                    vehicles_by_subclass[subclass].append(consist)
                else:
                    vehicles_by_subclass[subclass] = [consist]
        # reformat to a list we can then sort so order is consistent
        result = [{'name': i.__name__, 'doc': i.__doc__, 'class_obj': subclass, 'vehicles': vehicles_by_subclass[i]} for i in vehicles_by_subclass]
        return sorted(result, key=lambda subclass: subclass['name'])

    def get_engine_consists(self):
        result = []
        for i in self.get_vehicles_by_subclass(filter_subclasses_by_name='EngineConsist').values():
            result.extend(i)
        return result

    def fetch_prop(self, result, prop_name, value):
        result['vehicle'][prop_name] = value
        result['subclass_props'].append(prop_name)
        return result

    def unpack_name_string(self, consist):
        substrings = consist.name.split('string(')
        # engines have an untranslated name defined via _name, wagons use a translated string
        if consist._name is not None:
            name = consist._name
        else:
            # strip out spaces and some nml boilerplate to get the string name in isolation
            name_substr = substrings[2].translate({ord(c):'' for c in '), '})
            name = base_lang_strings[name_substr]
        # !! this would be better generalised to 'consist.has_suffix', currently docs rendering is knowing too much about the internals of trains
        if getattr(consist, 'subtype', None) is not 'U':
            suffix = base_lang_strings[substrings[3][0:-2]]
            return name + ' (' + suffix + ')'
        else:
            return name

    def get_props_to_print_in_code_reference(self, subclass):
        props_to_print = {}
        for vehicle in subclass['vehicles']:
            result = {'vehicle': {}, 'subclass_props': []}
            result = self.fetch_prop(
                result, 'Vehicle Name', self.unpack_name_string(vehicle))
            result = self.fetch_prop(result, 'Gen', vehicle.gen)
            result = self.fetch_prop(result, 'Railtype', vehicle.track_type)
            result = self.fetch_prop(result, 'HP', int(vehicle.power))
            result = self.fetch_prop(result, 'Speed (mph)', vehicle.speed)
            result = self.fetch_prop(result, 'Weight (t)', vehicle.weight)
            result = self.fetch_prop(
                result, 'TE coefficient', vehicle.tractive_effort_coefficient)
            result = self.fetch_prop(result, 'Intro Date', vehicle.intro_date)
            result = self.fetch_prop(
                result, 'Vehicle Life', vehicle.vehicle_life)
            result = self.fetch_prop(result, 'Buy Cost', vehicle.buy_cost)
            result = self.fetch_prop(
                result, 'Running Cost', vehicle.running_cost)
            #result = self.fetch_prop(result, 'Loading Speed', vehicle.loading_speed)

            props_to_print[vehicle] = result['vehicle']
            props_to_print[subclass['name']] = result['subclass_props']
        return props_to_print

    def get_base_numeric_id(self, consist):
        return consist.base_numeric_id

    def get_active_nav(self, doc_name, nav_link):
        return ('', 'active')[doc_name == nav_link]


def render_docs(doc_list, file_type, use_markdown=False):
    for doc_name in doc_list:
        # .pt is the conventional extension for chameleon page templates
        template = docs_templates[doc_name + '.pt']
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
        doc_file = codecs.open(os.path.join(
            docs_output_path, subdir, doc_name + '.' + file_type), 'w', 'utf8')
        doc_file.write(doc)
        doc_file.close()


def render_docs_images():
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs

    doc_helper = DocHelper()

    vehicle_graphics_src = os.path.join(currentdir, 'generated', 'graphics')
    for consist in consists:
        vehicle_spritesheet = Image.open(os.path.join(vehicle_graphics_src, consist.id + '.png'))
        source_vehicle_image = Image.new("P", (doc_helper.buy_menu_sprite_width(consist), doc_helper.buy_menu_sprite_height), 255)
        source_vehicle_image.putpalette(Image.open('palette_key.png').palette)

        if not consist.dual_headed:
            source_vehicle_image_tmp = vehicle_spritesheet.crop(box=(consist.buy_menu_x_loc,
                                                                     10,
                                                                     consist.buy_menu_x_loc + doc_helper.buy_menu_sprite_width(consist),
                                                                     10 + doc_helper.buy_menu_sprite_height))
        if consist.dual_headed:
            # oof, super special handling of dual-headed vehicles, OpenTTD handles this automatically in the buy menu, but docs have to handle explicitly
            # !! hard-coded values might fail in future, sort that out then if needed, they can be looked up in global constants
            source_vehicle_image_1 = vehicle_spritesheet.copy().crop(box=(224,
                                                                          10,
                                                                          224 + (4 * consist.length) + 1,
                                                                          10 + doc_helper.buy_menu_sprite_height))
            source_vehicle_image_2 = vehicle_spritesheet.copy().crop(box=(104,
                                                                          10,
                                                                          104 + (4 * consist.length) + 1,
                                                                          10 + doc_helper.buy_menu_sprite_height))
            source_vehicle_image_tmp = source_vehicle_image.copy()
            source_vehicle_image_tmp.paste(source_vehicle_image_1, (0,
                                                                    0,
                                                                    source_vehicle_image_1.width,
                                                                    doc_helper.buy_menu_sprite_height))
            source_vehicle_image_tmp.paste(source_vehicle_image_2, (source_vehicle_image_1.width - 1,
                                                                    0,
                                                                    source_vehicle_image_1.width - 1 + source_vehicle_image_2.width,
                                                                    doc_helper.buy_menu_sprite_height))
        crop_box_dest = (0,
                         0,
                         doc_helper.buy_menu_sprite_width(consist),
                         doc_helper.buy_menu_sprite_height)
        source_vehicle_image.paste(source_vehicle_image_tmp.crop(crop_box_dest), crop_box_dest)

        # add pantographs if needed
        if consist.pantograph_type is not None:
            # !! this doesn't handle the dual head case yet eh, blah blah, wasn't needed when coding it
            # buy menu uses pans 'down', but in docs pans 'up' looks better, weird eh?
            pantographs_spritesheet = Image.open(os.path.join(vehicle_graphics_src, consist.id + '_pantographs_up.png'))
            pantographs_image = pantographs_spritesheet.crop(box=(consist.buy_menu_x_loc,
                                                                  10,
                                                                  consist.buy_menu_x_loc + doc_helper.buy_menu_sprite_width(consist),
                                                                  10 + doc_helper.buy_menu_sprite_height))
            pantographs_mask = pantographs_image.copy()
            pantographs_mask = pantographs_mask.point(lambda i: 0 if i == 255 or i == 0 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato
            source_vehicle_image.paste(pantographs_image.crop(crop_box_dest), crop_box_dest, pantographs_mask.crop(crop_box_dest))

        # recolour to more pleasing CC combos
        cc_remap_1 = {198: 179, 199: 180, 200: 181, 201: 182, 202: 183, 203: 164, 204: 165, 205: 166,
                      80: 8, 81: 9, 82: 10, 83: 11, 84: 12, 85: 13, 86: 14, 87: 15}
        cc_remap_2 = {80: 198, 81: 199, 82: 200, 83: 201, 84: 202, 85: 203, 86: 204, 87: 205}
        for colour_name, cc_remap in {'red': cc_remap_1, 'blue': cc_remap_2}.items():
            processed_vehicle_image = source_vehicle_image.copy().point(lambda i: cc_remap[i] if i in cc_remap.keys() else i)

            # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
            processed_vehicle_image = processed_vehicle_image.resize((4 * processed_vehicle_image.width, 4 * doc_helper.buy_menu_sprite_height),
                                                                     resample=Image.NEAREST)
            output_path = os.path.join(images_dir_dst, consist.id + '_' + colour_name + '.png')
            processed_vehicle_image.save(
                output_path, optimize=True, transparency=0)


def main():
    start = time()
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

    print(format((time() - start), '.2f') + 's')


if __name__ == '__main__':
    main()
