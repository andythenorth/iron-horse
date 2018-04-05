# wagon ids are generic and are composed to specific vehicle ids elsewhere
# order is significant
buy_menu_sort_order_wagons = ['metro_car',
                              'passenger_car',
                              'luxury_passenger_car',
                              'mail_car',
                              'open_car',
                              'box_car',
                              'flat_car',
                              'hopper_car',
                              'dump_car',
                              'tank_car',
                              'covered_hopper_car',
                              'silo_car',
                              'livestock_car',
                              'edibles_tank_car',
                              'reefer_car',
                              'fruit_veg_car',
                              'intermodal_car',
                              'stake_car',
                              'supplies_car',
                              'vehicle_transporter_car',
                              'metal_car',
                              'caboose_car']

# occasionally label refits need to be shared across vehicle classes
allowed_refits_by_label = {'box_freight': [
    'MAIL', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN', 'NITR']}

# capacity multipliers for user-configurable capacity parameter
capacity_multipliers = [0.67, 1, 1.33]
# identifier for user-configurable capacity parameter
param_adjust_vehicle_capacity = 1

grfid = r"CA\12\1F"

# cargo aging constant - OTTD default is 185
CARGO_AGE_PERIOD = 185

# standard offsets for trains
default_spritesheet_offsets = {'3': [[-3, -25], [-3, -21], [0, -12], [5, -17], [-3, -14], [-14, -17], [-16, -12], [-8, -23]],
                               '4': [[-3, -26], [-6, -20], [0, -12], [0, -16], [-3, -18], [-14, -16], [-16, -12], [-8, -20]],
                               '5': [[-3, -22], [-6, -19], [0, -12], [1, -16], [-3, -14], [-16, -16], [-16, -12], [-8, -21]],
                               '6': [[-3, -22], [-8, -18], [-8, -12], [-4, -16], [-3, -14], [-14, -16], [-16, -12], [-8, -19]],
                               '7': [[-3, -20], [-8, -18], [0, -12], [-1, -15], [-3, -14], [-17, -15], [-16, -12], [-10, -19]],
                               '8': [[-3, -20], [-10, -17], [-16, -12], [-4, -15], [-3, -13], [-17, -14], [-16, -12], [-10, -18]]}

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes_asymmetric_unreversed = [(60, 8, 29), (73, 26, 24), (104, 33, 16), (143, 26, 24),
                                                    (180, 8, 29), (193, 26, 24), (224, 33, 16), (263, 26, 24)]

spritesheet_bounding_boxes_asymmetric_reversed = list(
    spritesheet_bounding_boxes_asymmetric_unreversed[4:8])
spritesheet_bounding_boxes_asymmetric_reversed.extend(
    spritesheet_bounding_boxes_asymmetric_unreversed[0:4])

# pick the RHS block of sprites, I prefer drawing on that side :P
spritesheet_bounding_boxes_symmetric_unreversed = list(
    spritesheet_bounding_boxes_asymmetric_unreversed[4:8])
spritesheet_bounding_boxes_symmetric_unreversed.extend(
    spritesheet_bounding_boxes_asymmetric_unreversed[4:8])

# spritesheet_bounding_boxes_symmetric_reversed is identical to symmetric unreversed
# (reversing symmetrical vehicles is meaningless, but used for livery hax when some vehicles are flipped)
spritesheet_bounding_boxes_symmetric_reversed = spritesheet_bounding_boxes_symmetric_unreversed

# rather than total spritesheet width, we often need to know the max x extent that actually contains sprites
# this is calculated from bounding boxes
sprites_max_x_extent = spritesheet_bounding_boxes_asymmetric_unreversed[
    7][0] + spritesheet_bounding_boxes_asymmetric_unreversed[7][1]

# these only used in docs as of April 2018; buy menu sprites in the grf refactored to work differently; consider moving these constants to render_docs
# was 36; now 33 is correct, but some spritesheets might have wrong widths due to copy-paste history etc
buy_menu_sprite_width = 33
buy_menu_sprite_height = 16

# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# done this way so we don't have to pass Polar Fox to templates, we can just pass global_constants
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox.constants
base_refits_by_class = polar_fox.constants.base_refits_by_class
cargo_labels = polar_fox.constants.cargo_labels
chameleon_cache_dir = polar_fox.constants.chameleon_cache_dir
default_cargos = polar_fox.constants.default_cargos
disallowed_refits_by_label = polar_fox.constants.disallowed_refits_by_label
generated_files_dir = polar_fox.constants.generated_files_dir
graphics_path = polar_fox.constants.graphics_path
mail_multiplier = polar_fox.constants.mail_multiplier
max_game_date = polar_fox.constants.max_game_date
