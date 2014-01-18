import os.path
currentdir = os.curdir
import sys

sys.path.append(os.path.join('gestalts')) # add to the module search path

from gestalts import cargo_coils
from gestalts import cargo_tarps

from gestalts import box_body
from gestalts import flat_body
from gestalts import tank_body
from gestalts import tipping_body
from gestalts import fifth_wheel_mask_body

from gestalts import truck
from gestalts import trailer

gestalt_patterns = {
    'cargo_coils': cargo_coils,
    'cargo_tarps': cargo_tarps,
    'body_box': box_body,
    'body_flat': flat_body,
    'body_tank': tank_body,
    'body_tipping': tipping_body,
    'body_fifth_wheel': fifth_wheel_mask_body,
    'trailer': trailer,
    'truck': truck,
}

def dispatch(filename):
    gestalt_full_id = filename.split('-',1)[0]
    for gestalt, module in gestalt_patterns.iteritems():
        if gestalt_full_id.startswith(gestalt):
            module.generate(filename)
