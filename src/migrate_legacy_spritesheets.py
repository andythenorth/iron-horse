import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import iron_horse
import global_constants
from pixa import Spritesheet
from PIL import Image

consists = iron_horse.get_consists_in_buy_menu_order()
base_template_spritesheet = Image.open(os.path.join('src','base_10_8_spritesheet.png'))
spriterow_height = 30

def get_legacy_bounding_boxes(y=0):
    return ([60,  y, 8, 27], [76,  y, 26, 24], [107, y, 40, 16], [156, y, 26, 24],
            [188, y, 8, 27], [200, y, 26, 24], [235, y, 40, 16], [284, y, 26, 24])

def detect_spriterows_with_content(file_path):
    legacy_spritesheet = Image.open(file_path)
    base_y = 10
    rows_with_valid_content = []
    while base_y < legacy_spritesheet.size[1]:
        crop_box = (0,
                    base_y,
                    legacy_spritesheet.size[0],
                    base_y + spriterow_height)
        test_row = legacy_spritesheet.crop(crop_box)
        base_y += spriterow_height
        if min(list(test_row.getdata())) < 255:
            # row contains some colours other than white, now check if it contains any blue, or if it's just leftover parts from drawing
            if min(list(test_row.getdata())) > 0:
                # this is just leftover parts, so show this image so it can be cleaned up manually
                test_row.show()
                print(file_path, "contains some orphaned / leftover / junk pixels")
            else:
                rows_with_valid_content.append(test_row)
    print(file_path, rows_with_valid_content)


legacy_file_paths = []
for consist in consists:
    if consist.use_legacy_spritesheet:
        # assumes spritesheets are suffixed _0 or _1, which is probably true
        for i in range(2):
            # non-template case
            file_path = os.path.join('src', 'graphics', consist.id + '_' + str(i) + '.png')
            if os.path.isfile(file_path):
                legacy_file_paths.append(file_path)
            # template case
            file_path = os.path.join('src', 'graphics', consist.id + '_template_' + str(i) + '.png')
            if os.path.isfile(file_path):
                legacy_file_paths.append(file_path)
legacy_file_paths.sort()

#for path in legacy_file_paths:
#detect_spriterows_with_content(legacy_file_paths[0])
detect_spriterows_with_content('src/graphics/cargo_sprinter_template_0.png')

print('Count', len(legacy_file_paths))
