from collections import OrderedDict

# wagon ids are generic and are composed to specific vehicle ids elsewhere
# order is significant
buy_menu_sort_order_wagons = ['alignment_car',
                              'hst_passenger_car',
                              'passenger_railcar_trailer_car',
                              'passenger_car',
                              'luxury_passenger_car',
                              'mail_car',
                              'express_car',
                              'express_intermodal_car',
                              'intermodal_car',
                              'open_car',
                              'box_car',
                              'curtain_side_box_car',
                              'sliding_wall_car',
                              'plate_car',
                              'flat_car',
                              'tarpaulin_car',
                              'coil_car',
                              'stake_car',
                              'hopper_car',
                              'rock_hopper_car',
                              'ore_hopper_car',
                              'dump_car',
                              'dump_car_high_side',
                              'scrap_metal_car',
                              'tank_car',
                              'product_tank_car',
                              'cryo_tank_car',
                              'covered_hopper_car',
                              'grain_hopper_car',
                              'pellet_hopper_car',
                              'silo_car',
                              'cement_silo_car',
                              'livestock_car',
                              'edibles_tank_car',
                              'reefer_car',
                              'fruit_veg_car',
                              #'well_car',
                              'carbon_black_hopper_car',
                              'vehicle_transporter_car',
                              'torpedo_car',
                              'slag_ladle_car',
                              'caboose_car']

# capacity multipliers for user-configurable capacity parameter
capacity_multipliers = [0.67, 1, 1.33]
# identifier for user-configurable capacity parameter
param_adjust_vehicle_capacity = 1

grfid = r"CA\12\1F"

# cargo aging constant - OTTD default is 185
CARGO_AGE_PERIOD = 185
# setting bonuses has limited effect on pax payment over 0-256 tile routes (might show up on longer routes)
# so instead set a malus, this nerfs standard pax so are relatively less profitable above somewhere around 64-128 tiles
CARGO_AGE_PERIOD_STANDARD_PAX_MALUS = 56
# metro mail and pax gets a total nerf, only use it on short routes
CARGO_AGE_PERIOD_METRO_MALUS = 32

# buy and run cost base factors
PR_BUILD_VEHICLE_TRAIN = -2
PR_BUILD_VEHICLE_WAGON = 1
# running cost multipliers nerfed down to makes smaller base cost incremements available
# the vehicle cost factor is then set high (using cb) to get a sensible final cost (but with fine-grained control)
# NOTE: all engines use RUNNING_COST_STEAM, and steam/diesel/electric variations are handled internally in Iron Horse
PR_RUNNING_TRAIN_STEAM = -2
# NOTE: all wagons use RUNNING_COST_DIESEL, nerfed down to small increments, for fine-grained control over low wagon run costs
PR_RUNNING_TRAIN_DIESEL = -4

# generalised mapping of roles to groups
# order is significant, so OrderedDict is used (this wouldn't be necessary for python >= 3.7, but at time of writing compile uses python 3.5)
role_group_mapping = OrderedDict([('express', ['branch_express_1', 'branch_express_2', 'express_1', 'express_2', 'heavy_express_1', 'heavy_express_2', 'heavy_express_3', 'heavy_express_4']),
                                  ('driving_cab', ['driving_cab_express_1']),
                                  ('freight', ['branch_freight', 'freight_1', 'freight_2', 'heavy_freight_1', 'heavy_freight_2', 'heavy_freight_3', 'heavy_freight_4']),
                                  ('universal', ['universal', 'mail_railcar_1', 'mail_railcar_2', 'pax_railcar_1', 'pax_railcar_2']),
                                  ('luxury_railcar', ['luxury_pax_railcar']),
                                  ('hst', ['hst']),
                                  ('very_high_speed', ['very_high_speed']),
                                  ('lolz', ['gronk!', 'snoughplough!']),
                                  ('metro', ['mail_metro', 'pax_metro'])])

# keep alphabetised, order not significant
role_string_mapping = {'driving_cab': 'STR_ROLE_DRIVING_CAB',
                       'express': 'STR_ROLE_GENERAL_PURPOSE_EXPRESS',
                       'freight': 'STR_ROLE_FREIGHT',
                       'hst': 'STR_ROLE_HST',
                       'lolz': 'STR_ROLE_LOLZ',
                       'luxury_railcar': 'STR_ROLE_GENERAL_PURPOSE_EXPRESS',
                       'metro': 'STR_ROLE_METRO',
                       'very_high_speed': 'STR_ROLE_VERY_HIGH_SPEED',
                       'universal': 'STR_ROLE_GENERAL_PURPOSE'}

# days offset is used to control *synchronising* (or not) intro dates across groups of vehicles where needed
# see https://github.com/OpenTTD/OpenTTD/pull/7147 for explanation
# the actual values will be translated into months later
# keep ordered by offset integer for ease of reading
intro_date_offsets_by_role_group = {'universal': 0,
                                    'express_core': 1,
                                    'express_non_core': 2,
                                    'driving_cab': 2,
                                    'hst': 3,
                                    'freight_core': 4,
                                    'freight_non_core': 5,
                                    'railcar': 6,
                                    'metro': 7,
                                    'very_high_speed': 8,
                                    'food_wagons': 9,
                                    'non_core_wagons': 10,
                                    'lolz': 11}

# up to 127 temp storages are available, might as well allocate them exclusively within the graphics chain to avoid any collisions
temp_storage_ids = dict(var_id_of_neighbouring_vehicle = 0, # used to avoid expensively reading var 61 multiple times, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_1 = 1, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_2 = 2, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_3 = 3, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_4 = 4, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_5 = 5, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_6 = 6, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_7 = 7, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_8 = 8, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_9 = 9, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_10 = 10, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_11 = 11, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_12 = 12, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_13 = 13, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_14 = 14, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_15 = 15, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_id_to_match_16 = 16, # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
                        var_num_vehs_in_vehid_chain_multiple_ids = 17, # alternative to num_vehs_in_vehid_chain (0x41), handling multiple IDs not one
                        var_position_in_vehid_chain_multiple_ids = 18, # alternative to num_vehs_in_vehid_chain (0x41), handling multiple IDs not one
                        var_position_in_vehid_chain_from_end_multiple_ids = 19 # alternative to num_vehs_in_vehid_chain (0x41), handling multiple IDs not one
                    )

# standard offsets for trains
default_spritesheet_offsets = {'3': [[-3, -26],  [ -6, -20], [  4, -12], [ 6, -15], [-3, -16], [-16, -15], [-16, -12], [-4, -20]],
                               '4': [[-3, -24],  [ -8, -19], [  0, -12], [ 4, -15], [-3, -16], [-16, -15], [-16, -12], [-4, -19]],
                               '5': [[-3, -22],  [-10, -18], [ -4, -12], [ 2, -15], [-3, -16], [-16, -15], [-16, -12], [-4, -18]],
                               '6': [[-3, -20],  [-12, -17], [ -8, -12], [ 0, -15], [-3, -16], [-16, -15], [-16, -12], [-4, -17]],
                               '7': [[-3, -18],  [-14, -16], [-12, -12], [-2, -15], [-3, -16], [-16, -15], [-16, -12], [-4, -16]],
                               '8': [[-3, -16],  [-16, -15], [-16, -12], [-4, -15], [-3, -16], [-16, -15], [-16, -12], [-4, -15]]}

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

# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# done this way so we don't have to pass Polar Fox to templates, we can just pass global_constants
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox.constants
base_refits_by_class = polar_fox.constants.base_refits_by_class
cargo_labels = polar_fox.constants.cargo_labels
chameleon_cache_dir = polar_fox.constants.chameleon_cache_dir
generated_files_dir = polar_fox.constants.generated_files_dir
graphics_path = polar_fox.constants.graphics_path
mail_multiplier = polar_fox.constants.mail_multiplier
max_game_date = polar_fox.constants.max_game_date
