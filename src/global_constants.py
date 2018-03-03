from polar_fox import base_refits_by_class, cargo_labels, disallowed_refits_by_label, chameleon_cache_dir, generated_files_dir, graphics_path, max_game_date

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
allowed_refits_by_label = {'box_freight': ['MAIL', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN', 'NITR']}

# capacity multipliers for user-configurable capacity parameter
capacity_multipliers = [0.67, 1, 1.33]
# identifier for user-configurable capacity parameter
param_adjust_vehicle_capacity = 1
# mailbags are < 1t, multiply capacity appropriately
mail_multiplier = 2

grfid = r"CA\12\1F"

# cargo aging constant - OTTD default is 185
CARGO_AGE_PERIOD = 185

# standard offsets for trains
default_spritesheet_offsets = {'3': [[-3, -25], [-3, -21], [-16, -12], [5, -17], [-3, -14], [-14, -17], [-16, -12], [-8, -23]],
                               '4': [[-3, -23], [-4, -20], [-16, -12], [3, -17], [-3, -14], [-14, -17], [-16, -12], [-8, -22]],
                               '5': [[-3, -22], [-6, -19], [-16, -12], [1, -16], [-3, -14], [-16, -16], [-16, -12], [-8, -21]],
                               '6': [[-3, -22], [-8, -18], [-16, -12], [-1, -15], [-3, -14], [-16, -15], [-16, -12], [-8, -19]],
                               '7': [[-3, -20], [-8, -18], [-16, -12], [-1, -15], [-3, -14], [-17, -15], [-16, -12], [-10, -19]],
                               '8': [[-3, -20], [-10, -17], [-16, -12], [-4, -15], [-3, -13], [-17, -14], [-16, -12], [-10, -18]]}

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes = ((60, 8, 29), (76, 26, 24), (107, 40, 16), (156, 26, 24),
                              (188, 8, 29), (200, 26, 24), (235, 40, 16), (284, 26, 24))

buy_menu_sprite_width = 36 # 36 is correct, but some spritesheets might have wrong widths due to copy-pasteo etc
buy_menu_sprite_height = 16