import os.path
import sys
sys.path.append(os.path.join("src"))  # add to the module search path

from PIL import Image
from polar_fox import pixa
from polar_fox import graphics_units

# requires a tmp dir to exist, which should be gitignored
# set the filename
input_filenames = [
    "log_car_pony_gen_5C",
    "log_car_ng_pony_gen_1U",
    "log_car_ng_pony_gen_3U",
    "log_car_ng_pony_gen_4U",
    "log_car_pony_gen_2A",
    "log_car_pony_gen_3A",
    "log_car_pony_gen_3B",
    "log_car_pony_gen_4A",
    "log_car_pony_gen_4B",
    "log_car_pony_gen_4C",
    "log_car_pony_gen_5B",
]

for input_filename in input_filenames:
    source_image = Image.open(os.path.join("tmp", input_filename + ".png"))

    spritesheet = pixa.make_spritesheet_from_image(source_image, graphics_units.DOS_PALETTE)

    processed_spritesheet = graphics_units.SwapCompanyColours().render(spritesheet)

    processed_spritesheet.sprites.save(os.path.join("tmp", input_filename + "_remapped.png"))
