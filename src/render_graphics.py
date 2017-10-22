#!/usr/bin/env python

print("[RENDER GRAPHICS] render_graphics.py")

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os
currentdir = os.curdir
from multiprocessing import Pool
import multiprocessing
logger = multiprocessing.log_to_stderr()
logger.setLevel(25)

import iron_horse
import utils
import global_constants

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)
num_pool_workers = makefile_args.get('num_pool_workers', 0) # default to no mp, makes debugging easier (mp fails to pickle errors correctly)
if num_pool_workers == 0:
    use_multiprocessing = False
else:
    use_multiprocessing = True

graphics_input = os.path.join(currentdir, 'src', 'graphics')
graphics_output_path = os.path.join(iron_horse.generated_files_path, 'graphics')
if os.path.exists(graphics_output_path):
    shutil.rmtree(graphics_output_path)
os.mkdir(graphics_output_path)

hint_file = codecs.open(os.path.join(graphics_output_path, '_graphics_files_here_are_generated.txt'), 'w','utf8')
hint_file.write("Don't edit the graphics files here.  They're generated by the build script. \n Edit sources in graphics_sources and export spritesheets to graphics_input.")
hint_file.close()

def run_pipeline(items):
    variant = items[0]
    consist = items[1]
    if variant.graphics_processor is None:
        shutil.copy(os.path.join(graphics_input, consist.roster_id, variant.get_spritesheet_name(consist)), graphics_output_path)
    else:
        result = variant.graphics_processor.pipeline.render(variant, consist, global_constants)
        return result

# wrapped in a main() function so this can be called explicitly, because unexpected multiprocessing fork bombs are bad
def main():
    start = time()
    print("[RENDER GRAPHICS] render_graphics.py")
    consists = iron_horse.get_consists_in_buy_menu_order()

    variants = []
    for consist in consists:
        spritesheet_suffixes_seen = []
        for variant in consist.model_variants:
            # raise if spritesheet_suffix number is a duplicate
            if variant.spritesheet_suffix in spritesheet_suffixes_seen:
                raise AssertionError("Duplicate spritesheet suffix in consist " + consist.id + ": " + str(variant.spritesheet_suffix))
            else:
                spritesheet_suffixes_seen.append(variant.spritesheet_suffix)
            variants.append((variant, consist))

    if use_multiprocessing == False:
        utils.echo_message('Multiprocessing disabled: (pw=0)')
        for variant in variants:
            run_pipeline(variant)
    else:
        pool = Pool(processes=num_pool_workers)
        pool.map(run_pipeline, variants)
        pool.close()

    print(format((time() - start), '.2f')+'s')

if __name__ == '__main__':
    main()
