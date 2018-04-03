import os.path
currentdir = os.curdir
import sys
sys.path.append(os.path.join('src')) # add to the module search path
import shutil
from PIL import Image, ImageDraw

import iron_horse
import global_constants
from rosters import registered_rosters

consists = iron_horse.get_consists_in_buy_menu_order()
input_graphics_dir = os.path.join('src', 'graphics')
output_graphics_dir = os.path.join('src', 'graphics_migrated')
"""
base_template_spritesheet = Image.open(os.path.join('graphics_sources','base_10_8_spritesheet.png'))
"""
spriterow_height = 30
DOS_PALETTE = Image.open('palette_key.png').palette

chassis_names = ['2_axle_filled_16px', '2_axle_filled_24px', '2_axle_gapped_16px', '2_axle_sparse_16px',
                 '4_axle_gapped_24px', '4_axle_gapped_32px', 'test']

def get_legacy_bounding_boxes(y=0):
    return [[60,  y, 8, 29], [76,  y, 26, 24], [107, y, 33, 16], [156, y, 26, 24],
            [188, y, 8, 29], [200, y, 26, 24], [235, y, 33, 16], [284, y, 26, 24]]

def new_legacy_bounding_boxes(y=0):
    return [[60,  y, 8, 29], [73,  y, 26, 24], [104, y, 33, 16], [143, y, 26, 24],
            [180, y, 8, 29], [193, y, 26, 24], [224, y, 33, 16], [263, y, 26, 24]]

def recomp_rows(spritesheet, rows_with_valid_content):
    #migrated_spriterow = base_template_spritesheet.crop((0, 10, 400, 40))
    fill_height = 10 + spriterow_height * len(rows_with_valid_content)
    fill = ImageDraw.Draw(spritesheet)
    fill.rectangle([0, 0, 310, fill_height], fill=255, outline=None)

    for row_count, spriterow in enumerate(rows_with_valid_content):
        # nothing yet
        for col_count, vertexes in enumerate(get_legacy_bounding_boxes()):
            crop_box = (vertexes[0], vertexes[1], vertexes[0] + vertexes[2], vertexes[1] + vertexes[3])
            sprite = spriterow.crop(crop_box)
            #sprite.show()
            col_insert_loc = new_legacy_bounding_boxes(10 + row_count * spriterow_height)[col_count]
            spritesheet.paste(sprite, (col_insert_loc[0], col_insert_loc[1]))
    return spritesheet

def detect_spriterows_with_content(filename, spritesheet):
    base_y = 10
    rows_with_valid_content = []

    while base_y + spriterow_height <= spritesheet.size[1]:
        crop_box = (0,
                    base_y,
                    310,
                    base_y + spriterow_height)
        test_row = spritesheet.crop(crop_box)
        base_y += spriterow_height
        only_blue_and_white = True
        for colour in list(test_row.getdata()):
            if colour > 0 and colour < 255:
                only_blue_and_white = False
        if not only_blue_and_white:
            # row contains _some_ colours other than white and blue, now check if it contains any blue, or if it's just leftover parts from drawing
            if min(list(test_row.getdata())) > 0:
                # there is no blue, this is just leftover parts, so show this image so it can be cleaned up manually
                #test_row.show()
                print(filename, "contains some orphaned / leftover / junk pixels")
            else:
                rows_with_valid_content.append(test_row)
                #test_row.show()
    return rows_with_valid_content

def main():
    print('[MIGRATING SPRITESHEETS]')
    if os.path.exists(output_graphics_dir):
        shutil.rmtree(output_graphics_dir)
    os.mkdir(output_graphics_dir)
    for roster in registered_rosters:
        os.mkdir(os.path.join(output_graphics_dir, roster.id))
    os.mkdir(os.path.join(output_graphics_dir, 'chassis'))

    for consist in consists:
        filename = os.path.join(consist.id + '.png')
        output_path = os.path.join(output_graphics_dir, consist.roster.id, filename)
        spritesheet = Image.open(os.path.join(input_graphics_dir, consist.roster.id, filename))
        rows_with_valid_content = detect_spriterows_with_content(filename, spritesheet)
        migrated_spritesheet = recomp_rows(spritesheet, rows_with_valid_content)
        #migrated_spritesheet.show()
        migrated_spritesheet.save(output_path)

    for chassis_name in chassis_names:
        filename = os.path.join(chassis_name + '.png')
        output_path = os.path.join(output_graphics_dir, 'chassis', filename)
        spritesheet = Image.open(os.path.join(input_graphics_dir, 'chassis', filename))
        rows_with_valid_content = detect_spriterows_with_content(filename, spritesheet)
        migrated_spritesheet = recomp_rows(spritesheet, rows_with_valid_content)
        migrated_spritesheet.save(output_path)

    print(len(consists) + len(chassis_names), 'spritesheets migrated')
    print('[DONE]')

if __name__ == '__main__':
    main()

