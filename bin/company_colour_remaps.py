import os.path
import sys
sys.path.append(os.path.join("src"))  # add to the module search path

from PIL import Image
from polar_fox import pixa
from polar_fox import graphics_units

# requires a tmp dir to exist, which should be gitignored
# set the filename
input_filenames = [
    "wyvern",
]

CC1 = 198

cc_remaps = {
    "obsidian": (1, 2, 24, 4, 5, 6, 7, 8),
    "faded_obsidian": (1, 70, 16, 4, 26, 6, 19, 8),
    "oil_black": (1, 2, 106, 4, 5, 6, 7, 8),
    "faded_oil_black": (1, 70, 106, 4, 18, 6, 20, 9),
    "nightshade": (104, 2, 25, 17, 18, 19, 20, 10),
    "light_nightshade": (1, 2, 106, 17, 18, 7, 20, 10),
}

cc_remaps_as_dicts = {
    name: {CC1 + i: value for i, value in enumerate(values)}
    for name, values in cc_remaps.items()
}

print(cc_remaps_as_dicts)

for input_filename in input_filenames:
    source_image = Image.open(os.path.join("tmp", input_filename + ".png"))

    spritesheet = pixa.make_spritesheet_from_image(source_image, graphics_units.DOS_PALETTE)

    processed_spritesheet = graphics_units.SwapCompanyColours().render(spritesheet)

    processed_spritesheet.sprites.save(os.path.join("tmp", input_filename + "_remapped_1CC_2CC_swap.png"))

    for cc_remap_name, cc_remap_values_dict in cc_remaps_as_dicts.items():
        spritesheet = pixa.make_spritesheet_from_image(source_image, graphics_units.DOS_PALETTE)
        processed_spritesheet = graphics_units.SimpleRecolour(cc_remap_values_dict).render(spritesheet)
        processed_spritesheet.sprites.save(os.path.join("tmp", input_filename + "_remapped_" + cc_remap_name + ".png"))
