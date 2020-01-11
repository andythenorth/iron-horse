import codecs  # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os
currentdir = os.curdir
import multiprocessing
from time import time
from PIL import Image
import markdown

import iron_horse
import utils
import global_constants

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()
metadata = {}
metadata['dev_thread_url'] = 'http://www.tt-forums.net/viewtopic.php?f=67&t=71219'
metadata['repo_url'] = 'http://dev.openttdcoop.org/projects/iron-horse/repository'
metadata['issue_tracker'] = 'http://dev.openttdcoop.org/projects/iron-horse/issues'

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

docs_src = os.path.join(currentdir, 'src', 'docs_templates')

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

    def get_vehicles_by_subclass(self, consists, filter_subclasses_by_name=None):
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

    def get_engines_by_roster_and_base_track_type(self, roster, base_track_type):
        result = []
        for consist in roster.engine_consists:
            if consist.base_track_type == base_track_type:
                result.append(consist)
        return result

    def get_wagons_by_roster_and_base_track_type(self, roster, base_track_type):
        result = []
        for wagon_class in global_constants.buy_menu_sort_order_wagons:
            for consist in roster.wagon_consists[wagon_class]:
                if consist.base_track_type == base_track_type:
                    result.append(consist)
        return result

    def get_roster_by_id(self, roster_id, registered_rosters):
        for roster in registered_rosters:
            if roster.id == roster_id:
                return roster
        # default result
        return None

    def engines_as_tech_tree_for_graphviz(self, consists):
        result = {}
        for base_track_type in self.get_base_track_types():
            result[base_track_type[0]] = {}
            for role in self.engine_roles(base_track_type, consists):
                role_engines = []
                fill_dummy = True
                intro_dates = self.get_roster_by_id('pony').intro_dates[base_track_type[0]]
                for gen, intro_date in enumerate(intro_dates, 1):
                    consist = self.get_engine_by_role_and_base_track_type_and_generation(role, base_track_type, gen)
                    engine_node = {}
                    # get the consist or a dummy node (for spacing the graph correctly by gen)
                    if consist is not None:
                        engine_node['id'] = consist.id
                        engine_node['label'] = self.unpack_name_string(consist).split('(')[0]
                        engine_node['image'] = consist.id + "_blue.png"
                        if consist.replacement_consist is not None:
                            fill_dummy = False # prevent adding any more dummy nodes after this real consist
                            engine_node['replacement_id'] = consist.replacement_consist.id
                        else:
                            if gen < len(intro_dates):
                                fill_dummy = True
                                engine_node['replacement_id'] = '_'.join(['dummy', base_track_type[0], role, str(gen + 1)])
                    else:
                        if fill_dummy:
                            engine_node['id'] = '_'.join(['dummy', base_track_type[0], role, str(gen)])
                            engine_node['label'] = 'dummy'
                            # figure out if there's a valid replacement
                            if gen < len(intro_dates):
                                next_gen_consist = self.get_engine_by_role_and_base_track_type_and_generation(role, base_track_type, gen + 1)
                                if next_gen_consist is not None:
                                    engine_node['replacement_id'] = next_gen_consist.id
                                else:
                                    engine_node['replacement_id'] = '_'.join(['dummy', base_track_type[0], role, str(gen + 1)])

                    if len(engine_node) != 0:
                        role_engines.append(engine_node)
                result[base_track_type[0]][role] = role_engines
        return result

    def engine_roles(self, base_track_type, consists, role_group=None):
        if role_group is None:
            print('role_group None passed - needs refactored')
            return []
        else:
            roles_ordered = global_constants.role_group_mapping[role_group]

        roles_to_include = []
        for consist in consists:
            if consist.base_track_type == base_track_type[0]:
                if consist.role is not None:
                    if consist.role in roles_ordered:
                        roles_to_include.append(consist.role)
        result = []
        for role in roles_ordered:
            if role in set(roles_to_include):
                result.append(role)
        return result

    def get_engine_by_role_and_base_track_type_and_generation(self, consists, role, base_track_type, gen):
        for consist in consists:
            if consist.role == role:
                if consist.base_track_type == base_track_type[0]:
                    if consist.gen == gen:
                        return consist
        # default result
        return None

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
        if getattr(consist, 'subtype', None) == 'U' and getattr(consist, 'str_name_suffix', None) != None:
            suffix = base_lang_strings[substrings[3][0:-2]]
            return name + ' (' + suffix + ')'
        else:
            return name

    def unpack_role_string_for_consist(self, consist):
        # strip off some nml boilerplate
        role_key = consist.buy_menu_role_string.replace('STR_ROLE, string(', '')
        role_key = role_key.replace(')', '')
        return base_lang_strings[role_key]

    def get_role_string_from_role(self, role):
        # mangle on some boilerplate to get the nml string
        for role_group, roles in global_constants.role_group_mapping.items():
            if role in roles:
                return base_lang_strings[global_constants.role_string_mapping[role_group]]

    def get_replaced_by_name(self, replacement_consist_id, consists):
        for consist in consists:
            if consist.id == replacement_consist_id:
                return self.unpack_name_string(consist)

    def get_props_to_print_in_code_reference(self, subclass):
        props_to_print = {}
        for vehicle in subclass['vehicles']:
            result = {'vehicle': {}, 'subclass_props': []}
            result = self.fetch_prop(
                result, 'Vehicle Name', self.unpack_name_string(vehicle))
            result = self.fetch_prop(result, 'Gen', vehicle.gen)
            if vehicle.role is not None:
                result = self.fetch_prop(result, 'Role', vehicle.role)
            result = self.fetch_prop(result, 'Railtype', vehicle.track_type)
            result = self.fetch_prop(result, 'HP', int(vehicle.power))
            result = self.fetch_prop(result, 'Speed (mph)', vehicle.speed)
            result = self.fetch_prop(result, 'HP/Speed ratio', vehicle.power_speed_ratio)
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

    def get_base_track_types(self):
        # tuple of pairs, need consistent order so can't use dict
        return (('RAIL', 'Standard Gauge'), ('NG', 'Narrow Gauge'), ('METRO', 'Metro'))

def render_docs(doc_list, file_type, docs_output_path, iron_horse, consists, use_markdown=False):
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader
    docs_templates = PageTemplateLoader(docs_src, format='text')

    for doc_name in doc_list:
        # .pt is the conventional extension for chameleon page templates
        template = docs_templates[doc_name + '.pt']
        doc = template(consists=consists, global_constants=global_constants, registered_rosters=iron_horse.registered_rosters, makefile_args=makefile_args,
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

def render_docs_images(consist):
    # process vehicle buy menu sprites for reuse in docs
    # extend this similar to render_docs if other image types need processing in future

    # vehicles: assumes render_graphics has been run and generated dir has correct content
    # I'm not going to try and handle that in python, makefile will handle it in production
    # for development, just run render_graphics manually before running render_docs

    doc_helper = DocHelper()

    vehicle_graphics_src = os.path.join(currentdir, 'generated', 'graphics')
    vehicle_spritesheet = Image.open(os.path.join(vehicle_graphics_src, consist.id + '.png'))
    # these 'source' var names for images are misleading
    source_vehicle_image = Image.new("P", (doc_helper.buy_menu_sprite_width(consist), doc_helper.buy_menu_sprite_height), 255)
    source_vehicle_image.putpalette(Image.open('palette_key.png').palette)

    if not consist.dual_headed:
        y_offset = consist.docs_image_spriterow * 30
        source_vehicle_image_tmp = vehicle_spritesheet.crop(box=(consist.buy_menu_x_loc,
                                                                 10 + y_offset,
                                                                 consist.buy_menu_x_loc + doc_helper.buy_menu_sprite_width(consist),
                                                                 10 + y_offset + doc_helper.buy_menu_sprite_height))
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
                                                                source_vehicle_image_1.size[0],
                                                                doc_helper.buy_menu_sprite_height))
        source_vehicle_image_tmp.paste(source_vehicle_image_2, (source_vehicle_image_1.size[0] - 1,
                                                                0,
                                                                source_vehicle_image_1.size[0] - 1 + source_vehicle_image_2.size[0],
                                                                doc_helper.buy_menu_sprite_height))
    crop_box_dest = (0,
                     0,
                     doc_helper.buy_menu_sprite_width(consist),
                     doc_helper.buy_menu_sprite_height)
    source_vehicle_image.paste(source_vehicle_image_tmp.crop(crop_box_dest), crop_box_dest)

    # add pantographs if needed
    if consist.pantograph_type is not None:
        # buy menu uses pans 'down', but in docs pans 'up' looks better, weird eh?
        pantographs_spritesheet = Image.open(os.path.join(vehicle_graphics_src, consist.id + '_pantographs_up.png'))
        pan_crop_width = global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[6][1]
        pantographs_image = pantographs_spritesheet.crop(box=(consist.buy_menu_x_loc,
                                                              10,
                                                              consist.buy_menu_x_loc + pan_crop_width,
                                                              10 + doc_helper.buy_menu_sprite_height))
        pantographs_mask = pantographs_image.copy()
        pantographs_mask = pantographs_mask.point(lambda i: 0 if i == 255 or i == 0 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato
        source_vehicle_image.paste(pantographs_image.crop(crop_box_dest), crop_box_dest, pantographs_mask.crop(crop_box_dest))

        if consist.dual_headed:
            # oof, super special handling of pans for dual-headed vehicles
            pan_start_x_loc = global_constants.spritesheet_bounding_boxes_asymmetric_unreversed[2][0]
            pantographs_image = pantographs_spritesheet.crop(box=(pan_start_x_loc,
                                                                  10,
                                                                  pan_start_x_loc + pan_crop_width,
                                                                  10 + doc_helper.buy_menu_sprite_height))
            crop_box_dest_pan_2 = (int(doc_helper.buy_menu_sprite_width(consist) / 2),
                                   0,
                                   int(doc_helper.buy_menu_sprite_width(consist) / 2) + pan_crop_width,
                                   doc_helper.buy_menu_sprite_height)
            pantographs_mask = pantographs_image.copy()
            pantographs_mask = pantographs_mask.point(lambda i: 0 if i == 255 or i == 0 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato
            source_vehicle_image.paste(pantographs_image, crop_box_dest_pan_2, pantographs_mask)
            pantographs_spritesheet.close()
    # recolour to more pleasing CC combos
    cc_remap_1 = {198: 179, 199: 180, 200: 181, 201: 182, 202: 183, 203: 164, 204: 165, 205: 166,
                  80: 8, 81: 9, 82: 10, 83: 11, 84: 12, 85: 13, 86: 14, 87: 15}
    cc_remap_2 = {80: 198, 81: 199, 82: 200, 83: 201, 84: 202, 85: 203, 86: 204, 87: 205}
    for colour_name, cc_remap in {'red': cc_remap_1, 'blue': cc_remap_2}.items():
        processed_vehicle_image = source_vehicle_image.copy().point(lambda i: cc_remap[i] if i in cc_remap.keys() else i)

        # oversize the images to account for how browsers interpolate the images on retina / HDPI screens
        processed_vehicle_image = processed_vehicle_image.resize((4 * processed_vehicle_image.size[0], 4 * doc_helper.buy_menu_sprite_height),
                                                                 resample=Image.NEAREST)
        output_path = os.path.join(currentdir, 'docs', 'html', 'static', 'img', consist.id + '_' + colour_name + '.png')
        processed_vehicle_image.save(output_path, optimize=True, transparency=0)
    source_vehicle_image.close()

def main():
    print("[RENDER DOCS] render_docs.py")
    start = time()
    iron_horse.main()

    # default to no mp, makes debugging easier (mp fails to pickle errors correctly)
    num_pool_workers = makefile_args.get('num_pool_workers', 0)
    if num_pool_workers == 0:
        use_multiprocessing = False
        # just print, no need for a coloured echo_message
        print('Multiprocessing disabled: (PW=0)')
    else:
        use_multiprocessing = True
        #logger = multiprocessing.log_to_stderr()
        #logger.setLevel(25)
        # just print, no need for a coloured echo_message
        print('Multiprocessing enabled: (PW=' + str(num_pool_workers) + ')')

    # setting up a cache for compiled chameleon templates can significantly speed up template rendering
    chameleon_cache_path = os.path.join(
        currentdir, global_constants.chameleon_cache_dir)
    if not os.path.exists(chameleon_cache_path):
        os.mkdir(chameleon_cache_path)
    os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

    docs_output_path = os.path.join(currentdir, 'docs')
    if os.path.exists(docs_output_path):
        shutil.rmtree(docs_output_path)
    os.mkdir(docs_output_path)

    shutil.copy(os.path.join(docs_src, 'index.html'), docs_output_path)

    static_dir_src = os.path.join(docs_src, 'html', 'static')
    static_dir_dst = os.path.join(docs_output_path, 'html', 'static')
    shutil.copytree(static_dir_src, static_dir_dst)

    # import iron_horse inside main() as it's so slow to import, and should only be imported explicitly
    consists = iron_horse.get_consists_in_buy_menu_order()
    # default sort for docs is by intro date
    consists = sorted(consists, key=lambda consist: consist.intro_date)
    dates = sorted([i.intro_date for i in consists])
    metadata['dates'] = (dates[0], dates[-1])

    # render standard docs from a list
    html_docs = ['trains', 'tech_tree_table_blue', 'tech_tree_table_red', 'code_reference', 'get_started', 'translations']
    txt_docs = ['license', 'readme']
    markdown_docs = ['changelog']
    graph_docs = ['tech_tree_linkgraph']

    render_docs(html_docs, 'html', docs_output_path, iron_horse, consists)
    render_docs(txt_docs, 'txt', docs_output_path, iron_horse, consists)
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, 'txt', docs_output_path, iron_horse, consists)
    render_docs(markdown_docs, 'html', docs_output_path, iron_horse, consists, use_markdown=True)
    render_docs(graph_docs, 'dotall', docs_output_path, iron_horse, consists)

    # process images for use in docs
    # yes, I really did bother using a pool to save at best a couple of seconds, because FML :)
    slow_start = time()
    if use_multiprocessing == False:
        for consist in consists:
            render_docs_images(consist)
    else:
        # Would this go faster if the pipelines from each consist were placed in MP pool, not just the consist?
        # probably potato / potato tbh
        pool = multiprocessing.Pool(processes=num_pool_workers)
        pool.map(render_docs_images, consists)
        pool.close()
        pool.join()
    print('render_docs_images', time() - slow_start)

    print(format((time() - start), '.2f') + 's')

if __name__ == '__main__':
    main()
