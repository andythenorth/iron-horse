print("[RENDER NML] render_nml.py")

import codecs  # used for writing files - more unicode friendly than standard open() module

import sys
import os
currentdir = os.curdir
from time import time

import iron_horse
import utils
import global_constants

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

# chameleon used in most template cases
from chameleon import PageTemplateLoader
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(
    currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

generated_files_path = iron_horse.generated_files_path

def render_header_item_nml(header_item, consists):
    template = templates[header_item + '.pynml']
    return utils.unescape_chameleon_output(template(consists=consists,
                                                    global_constants=global_constants,
                                                    temp_storage_ids=global_constants.temp_storage_ids, # convenience measure
                                                    utils=utils,
                                                    active_rosters=iron_horse.get_active_rosters(),
                                                    graphics_path=global_constants.graphics_path,
                                                    intermodal_containers=iron_horse.intermodal_containers,
                                                    haulage_bonus_engine_id_tree=iron_horse.get_haulage_bonus_engine_id_tree(),
                                                    pax_car_ids=iron_horse.get_pax_car_ids(),
                                                    livery_2_engine_ids=iron_horse.get_livery_2_engine_ids(),
                                                    makefile_args=makefile_args))

def render_consist_nml(consist):
    result = utils.unescape_chameleon_output(consist.render(templates))
    # write the nml per vehicle to disk, it aids debugging
    consist_nml = codecs.open(os.path.join(
        generated_files_path, 'nml', consist.id + '.nml'), 'w', 'utf8')
    consist_nml.write(result)
    consist_nml.close()
    # also return the nml directly for writing to the concatenated nml, don't faff around opening the generated nml files from disk
    return result

def main():
    start = time()
    iron_horse.main()
    print(iron_horse.vacant_numeric_ids_formatted())

    generated_nml_path = os.path.join(generated_files_path, 'nml')
    if not os.path.exists(generated_nml_path):
        # reminder to self: inside main() to avoid modifying filesystem simply by importing module
        os.mkdir(generated_nml_path)
    grf_nml = codecs.open(os.path.join(
        generated_files_path, 'iron-horse.nml'), 'w', 'utf8')

    consists = iron_horse.get_consists_in_buy_menu_order()

    header_items = ['header', 'cargo_table', 'railtype_table', 'spriteset_templates', 'tail_lights', 'intermodal_containers',
                    'procedures_capacity', 'procedures_colour_mapping', 'procedures_alternative_var_41', 'procedures_haulage_bonus', 'procedures_rulesets',
                    'procedures_box_car_with_opening_doors', 'procedures_consist_specific_liveries', 'procedures_visible_cargo']
    for header_item in header_items:
        grf_nml.write(render_header_item_nml(header_item, consists))

    # multiprocessing was tried here and removed as it was empirically slower in testing (due to overhead of starting extra pythons probably)
    for consist in consists:
        grf_nml.write(render_consist_nml(consist))

    grf_nml.close()

    print(format((time() - start), '.2f') + 's')


if __name__ == '__main__':
    main()
