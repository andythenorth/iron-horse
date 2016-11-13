import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path
import shutil

import iron_horse
import global_constants
from PIL import Image, ImageDraw

consists = iron_horse.get_consists_in_buy_menu_order()
input_graphics_dir = os.path.join('src', 'graphics')
output_graphics_dir = os.path.join('src', 'graphics_migrated')
base_template_spritesheet = Image.open(os.path.join('graphics_sources','base_10_8_spritesheet.png'))
spriterow_height = 30
DOS_PALETTE = Image.open('palette_key.png').palette

col_insertion_points = ([60,  4], [76,  2], [107, 1], [156, 2],
                        [188, 4], [200, 2], [235, 1], [284, 2],
                        [316, 1])

def get_legacy_bounding_boxes(y=0):
    return [[60,  y, 8, 25], [76,  y, 22, 22], [107, y, 32, 15], [156, y, 22, 22],
            [188, y, 8, 25], [204, y, 22, 22], [235, y, 32, 15], [284, y, 22, 22],
            [316, y, 64, 15]]

def recomp_legacy_spriterows(row_count, spriterow, migrated_spritesheet):
    migrated_spriterow = base_template_spritesheet.crop((0, 10, 400, 40))
    # we only want the first row to show blue bounding box for buy menu, so draw white rectangle over it for other rows
    if row_count > 0:
        replace_buy_menu_bb = ImageDraw.Draw(migrated_spriterow)
        replace_buy_menu_bb.rectangle([316, 0, 380, 40], 255)
    for col_count, vertexes in enumerate(get_legacy_bounding_boxes()):
        crop_box = (vertexes[0], vertexes[1], vertexes[0] + vertexes[2], vertexes[1] + vertexes[3])
        sprite = spriterow.crop(crop_box)
        #sprite.show()
        # don't paste if the sprite only contains blue or white
        only_blue_and_white = True
        for colour in list(sprite.getdata()):
            if colour > 0 and colour < 255:
                only_blue_and_white = False
        if not only_blue_and_white:
            col_insert_loc = col_insertion_points[col_count]
            migrated_spriterow.paste(sprite, (col_insert_loc[0], col_insert_loc[1]))
    row_insert_loc = (0, 10 + row_count * spriterow_height)
    migrated_spritesheet.paste(migrated_spriterow, row_insert_loc)
    return migrated_spritesheet

def migrate_spritesheet(rows_with_valid_content):
    new_height = 10 + spriterow_height * len(rows_with_valid_content)
    migrated_spritesheet = Image.new("P", (400, new_height), 255)
    migrated_spritesheet.putpalette(DOS_PALETTE)
    for row_count, spriterow in enumerate(rows_with_valid_content):
        migrated_spritesheet = recomp_legacy_spriterows(row_count, spriterow, migrated_spritesheet)
    return migrated_spritesheet

def detect_spriterows_with_content(filename):
    legacy_spritesheet = Image.open(os.path.join(input_graphics_dir, filename))
    base_y = 10
    rows_with_valid_content = []
    while base_y + spriterow_height < legacy_spritesheet.size[1]:
        crop_box = (0,
                    base_y,
                    legacy_spritesheet.size[0],
                    base_y + spriterow_height)
        test_row = legacy_spritesheet.crop(crop_box)
        base_y += spriterow_height

        only_blue_and_white = True
        for colour in list(test_row.getdata()):
            if colour > 0 and colour < 255:
                only_blue_and_white = False
        if not only_blue_and_white:
            # row contains _some_ colours other than white and blue, now check if it contains any blue, or if it's just leftover parts from drawing
            if min(list(test_row.getdata())) > 0:
                # there is no blue, this is just leftover parts, so show this image so it can be cleaned up manually
                test_row.show()
                print(filename, "contains some orphaned / leftover / junk pixels")
            else:
                rows_with_valid_content.append(test_row)
    return rows_with_valid_content

def main():
    if os.path.exists(output_graphics_dir):
        shutil.rmtree(output_graphics_dir)
    os.mkdir(output_graphics_dir)

    legacy_filenames = []
    for consist in consists:
        if consist.use_legacy_spritesheet:
            # assumes spritesheets are suffixed _0 or _1, which is probably true
            for i in range(2):
                # non-template case
                filename = os.path.join(consist.id + '_' + str(i) + '.png')
                if os.path.isfile(os.path.join(input_graphics_dir, filename)):
                    legacy_filenames.append(filename)
                # template case
                filename = os.path.join(consist.id + '_template_' + str(i) + '.png')
                if os.path.isfile(os.path.join(input_graphics_dir, filename)):
                    legacy_filenames.append(filename)
    legacy_filenames.sort()

    #legacy_filenames = ['cargo_sprinter_template_0.png'] # for testing a single vehicle when debugging
    for filename in legacy_filenames:
        output_path = os.path.join(output_graphics_dir, filename)
        rows_with_valid_content = detect_spriterows_with_content(filename)
        migrated_spritesheet = migrate_spritesheet(rows_with_valid_content)
        migrated_spritesheet.save(output_path)

    print('Migrated spritesheets count:', len(legacy_filenames))

if __name__ == '__main__':
    main()

