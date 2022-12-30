from collections import OrderedDict

# wagon ids are generic and are composed to specific vehicle ids elsewhere
# order is significant
buy_menu_sort_order_wagons = [
    "alignment_car",
    "hst_passenger_car",
    "hst_mail_car",
    "railbus_passenger_trailer_car",
    "railcar_passenger_trailer_car",
    "express_railcar_passenger_trailer_car",
    "passenger_car",
    "restaurant_car",
    "suburban_passenger_car",
    "mail_car",
    "express_car",
    "automobile_car",
    "low_floor_automobile_car",
    "double_deck_automobile_car",
    "express_intermodal_car",
    "intermodal_car",
    "low_floor_intermodal_car",
    "open_car",
    "merchandise_open_car",
    "hood_open_car",
    "box_car",
    "merchandise_box_car",
    "curtain_side_box_car",
    "sliding_wall_car",
    "vehicle_parts_box_car",
    "goods_box_car",
    "plate_car",
    "flat_car",
    "bulkhead_flat_car",
    "sliding_roof_car",
    "tarpaulin_car",
    "bolster_car",
    "coil_car_uncovered",
    "coil_car_covered",
    "hopper_car",
    "mgr_hopper_car",
    "rock_hopper_car",
    "mineral_hopper_car",
    "ore_hopper_car",
    "dump_car",
    "dump_car_high_side",
    "aggregate_car",
    "ore_dump_car",
    "scrap_metal_car",
    "skip_car",
    "tank_car",
    "product_tank_car",
    "acid_tank_car",
    "pressure_tank_car",
    "cryo_tank_car",
    "covered_hopper_car",
    "dry_powder_hopper_car",
    "mineral_covered_hopper_car",
    "roller_roof_hopper_car",
    "swing_roof_hopper_car",
    "chemical_covered_hopper_car",
    "silo_car",
    "chemical_silo_car",
    "cement_silo_car",
    "livestock_car",
    "edibles_tank_car",
    "reefer_car",
    "farm_products_box_car",
    "farm_products_hopper_car",
    "log_car",
    "kaolin_hopper_car",
    "carbon_black_hopper_car",
    "peat_car",
    #'well_car',
    "torpedo_car",
    "coil_buggy_car",
    "ingot_car",
    "slag_ladle_car",
    "randomised_open_car",
    "randomised_box_car",
    "randomised_piece_goods_car",
    "randomised_flat_car",
    "randomised_metal_coil_car",
    "randomised_hopper_car",
    "randomised_dump_car",
    "randomised_bulk_car",
    "randomised_chemicals_tank_car",
    "randomised_covered_hopper_car",
    "caboose_car",
]

# mapping of railtype labels to the vehicle track type names
# used when determining track_type property for vehicles
# the *first item* must be the actual label provided by an appropriate Iron Horse railtype
# the rest are fallbacks, in order, for use with other railtype grfs
# railtype authors need to be able to control mapping IHXX types to their preferred scheme, which they can do using railtype alternative_railtype_list property
# see the docs Code Reference page for further explanation of the Iron Horse label schema
# Standardised Railtype Scheme (SRS) labels are *only* to be used as *fallbacks*, and only where appropriate
# Iron Horse only partially complies with the SRS, using the Innsbruck 2022 Convention, where axle load is always set to A, equivalent to 'undefined'
# see https://newgrf-specs.tt-wiki.net/wiki/Standardized_Railtype_Scheme#.22Innsbruck_2022_Convention.22_for_partial_compliance
railtype_labels_by_vehicle_track_type_name = {
    "RAIL": ["IHA_", "RAIL"],
    "RAIL_ELECTRIFIED_AC": ["IHB_", "ELRL"],
    "RAIL_ELECTRIFIED_AC_DC": ["IHG_", "ELRL"],
    "RAIL_ELECTRIFIED_DC": ["IHF_"], # no fallback for DC if not present
    "RAIL_HIGH_CLEARANCE": ["IHAB"],
    "METRO": [
        "IHC_",
        "MTRO",
    ],  # no other fallbacks, metro is a segregated network, not just normal 3rd rail trains, and standardised scheme does not appear to support that case
    "NG": ["IHD_", "NGRL", "NAAN"],
    "NG_ELECTRIFIED_AC": ["IHE_", "ELNG", "NAAE"],
    "LGV": ["IHAA", "RAIL"],
    "LGV_ELECTRIFIED_AC": ["IHBA", "ELRL"],
}

# capacity multipliers for user-configurable capacity parameter
capacity_multipliers = [0.33, 0.67, 1, 1.33, 1.77]

metadata = {
    "dev_thread_url": "https://www.tt-forums.net/viewtopic.php?f=67&t=71219",
    "repo_url": "https://github.com/andythenorth/iron-horse",
    "docs_url": "https://grf.farm/iron-horse",
}

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
role_group_mapping = OrderedDict(
    [
        (
            "express",
            [
                "branch_express",
                "express",
                "heavy_express",
                "super_heavy_express",
                "ultra_heavy_express",
            ],
        ),
        (
            "high_power_railcar",
            [
                "high_power_railcar",
            ],
        ),
        (
            "driving_cab",
            [
                "driving_cab_express_pax",
                "driving_cab_express_mail",
                "driving_cab_express_mixed",
            ],
        ),
        (
            "freight",
            [
                "branch_freight",
                "freight",
                "heavy_freight",
                "super_heavy_freight",
                "ultra_heavy_freight",
            ],
        ),
        (
            "universal",
            # order of mailrailcar and pax_railbus is significant as of April 2021, for unfortunate tech-tree ordering reasons
            ["universal", "mail_railcar", "pax_railbus"],
        ),
        # railcars get their own special case due to high capacity, bit janky but eh
        (
            "suburban",
            ["pax_railcar", "pax_suburban_coach"],
        ),
        ("express_railcar", ["express_pax_railcar"]),
        ("hst", ["hst"]),
        ("very_high_speed", ["very_high_speed"]),
        (
            "lolz",
            [
                "gronk!",
                "snoughplough!",
            ],
        ),
        ("metro", ["pax_metro", "mail_metro"]),  # note pax before mail
    ]
)

# keep alphabetised, order not significant
role_string_mapping = {
    "driving_cab": "STR_ROLE_DRIVING_CAB",
    "express": "STR_ROLE_GENERAL_PURPOSE_EXPRESS",
    "freight": "STR_ROLE_FREIGHT",
    "high_power_railcar": "STR_ROLE_GENERAL_PURPOSE_EXPRESS",
    "hst": "STR_ROLE_HST",
    "lolz": "STR_ROLE_LOLZ",
    "express_railcar": "STR_ROLE_GENERAL_PURPOSE_EXPRESS",
    "metro": "STR_ROLE_METRO",
    "suburban": "STR_ROLE_SUBURBAN",
    "very_high_speed": "STR_ROLE_VERY_HIGH_SPEED",
    "universal": "STR_ROLE_GENERAL_PURPOSE",
}

# days offset is used to control *synchronising* (or not) intro dates across groups of vehicles where needed
# see https://github.com/OpenTTD/OpenTTD/pull/7147 for explanation
# the actual values will be translated into months later
# keep ordered by offset integer for ease of reading
intro_month_offsets_by_role_group = {
    "universal": 0,
    "express_core": 1,
    "express_non_core": 2,
    "express_railcar": 2,
    "high_power_railcar": 2,
    "driving_cab": 2,
    "hst": 3,
    "freight_core": 4,
    "freight_non_core": 5,
    "suburban": 6,
    "metro": 7,
    "very_high_speed": 8,
    "food_wagons": 9,
    "non_core_wagons": 10,
    "lolz": 11,
}

# custom remappings of cc1/cc2, used in recolour_sprites, not used in graphics generation, so not in graphics_constants
# post python 3.7, we rely on dict order being stable here, so we can get keys by position when we need to
custom_wagon_recolour_sprite_maps = {
    "custom_dark_brown": (105, 106, 33, 34, 35, 36, 37, 38),
    "custom_bauxite": (60, 61, 73, 62, 75, 76, 77, 78),
    "custom_dark_pink": (40, 41, 42, 43, 44, 45, 46, 47),
    "custom_light_pink": (43, 44, 45, 46, 47, 166, 167, 168),
    "custom_dark_grey": (3, 16, 17, 18, 19, 20, 21, 22),
    "custom_dark_yellow": (60, 61, 62, 64, 65, 66, 67, 68),
    "custom_dark_white": (18, 7, 8, 10, 11, 12, 13, 14),
    "custom_light_purple": (136, 170, 171, 172, 173, 174, 175, 176),
    "custom_light_mauve": (129, 130, 131, 132, 133, 134, 135, 14),
    "custom_dark_orange": (62, 63, 64, 193, 194, 195, 196, 197),
    "custom_dark_cream": (112, 113, 114, 116, 117, 118, 119, 120),
    "custom_green": (
        80,
        82,
        83,
        84,
        85,
        86,
        207,
        209,
    ),  # can't name it dark_green cos that conflates with DARK_GREEN
    "custom_blue": (
        147,
        148,
        149,
        150,
        151,
        152,
        153,
        210,
    ),  # can't name it dark_blue cos that conflates with DARK_BLUE
    "custom_light_blue": (
        155,
        156,
        157,
        158,
        159,
        160,
        161,
        210,
    ),  # can't name it dark_light_blue cos that would be silly
    "custom_dark_blue": (
        199,
        200,
        201,
        202,
        203,
        204,
        205,
        152,
    ),  # can't name it light_dark_blue cos that would be silly
    "custom_dark_red": (180, 181, 182, 183, 164, 165, 166, 167),
    "custom_pale_green": (97, 98, 99, 100, 101, 102, 103, 14),
    "custom_dark_green": (89, 90, 91, 92, 93, 94, 95, 31),
}

# up to 127 temp storages are available, might as well allocate them exclusively within the graphics chain to avoid any collisions
temp_storage_ids = dict(
    id_of_neighbouring_vehicle=0,  # used to avoid expensively reading var 61 multiple times, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_1=1,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_2=2,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_3=3,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_4=4,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_5=5,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_6=6,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_7=7,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_8=8,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_9=9,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_10=10,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_11=11,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_12=12,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_13=13,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_14=14,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_15=15,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    id_to_match_16=16,  # one of 16 temp storages which hold a list of IDs to match, used in re-implementation of var 41 to check multiple IDs not a single ID
    num_vehs_in_vehid_chain_multiple_ids=17,  # alternative to num_vehs_in_vehid_chain (0x41), handling multiple IDs not one
    position_in_vehid_chain_multiple_ids=18,  # alternative to num_vehs_in_vehid_chain (0x41), handling multiple IDs not one
    position_in_vehid_chain_from_end_multiple_ids=19,  # alternative to num_vehs_in_vehid_chain (0x41), handling multiple IDs not one
    cc_num_to_randomise=20,  # used in procedures_colour_randomisation_strategies
    auto_colour_randomisation_strategy_num=21,  # used in procedures_colour_randomisation_strategies
    use_wagon_base_colour_parameter=22,  # used in procedures_colour_randomisation_strategies
    unreversible_spritelayer_cargos=23,  # used to handle esoteric cases where spritelayer cargos need to reverse
    consist_specific_position_variant_num=24,  # used to store result of switch_graphics_pax_car_ruleset() and similar
)

# standard offsets for trains
default_spritesheet_offsets = {
    "2": [
        [-3, -28],
        [-4, -21],
        [8, -12],
        [8, -15],
        [-3, -16],
        [-16, -15],
        [-16, -12],
        [-4, -21],
    ],
    "3": [
        [-3, -26],
        [-6, -20],
        [4, -12],
        [6, -15],
        [-3, -16],
        [-16, -15],
        [-16, -12],
        [-4, -20],
    ],
    "4": [
        [-3, -24],
        [-8, -19],
        [0, -12],
        [4, -15],
        [-3, -16],
        [-16, -15],
        [-16, -12],
        [-4, -19],
    ],
    "5": [
        [-3, -22],
        [-10, -18],
        [-4, -12],
        [2, -15],
        [-3, -16],
        [-16, -15],
        [-16, -12],
        [-4, -18],
    ],
    "6": [
        [-3, -20],
        [-12, -17],
        [-8, -12],
        [0, -15],
        [-3, -16],
        [-16, -15],
        [-16, -12],
        [-4, -17],
    ],
    "7": [
        [-3, -18],
        [-14, -16],
        [-12, -12],
        [-2, -15],
        [-3, -16],
        [-16, -15],
        [-16, -12],
        [-4, -16],
    ],
    "8": [
        [-3, -16],
        [-16, -15],
        [-16, -12],
        [-4, -15],
        [-3, -16],
        [-16, -15],
        [-16, -12],
        [-4, -15],
    ],
}

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes_asymmetric_unreversed = [
    (60, 8, 29),
    (73, 26, 24),
    (104, 33, 16),
    (143, 26, 24),
    (180, 8, 29),
    (193, 26, 24),
    (224, 33, 16),
    (263, 26, 24),
]

spritesheet_bounding_boxes_asymmetric_reversed = list(
    spritesheet_bounding_boxes_asymmetric_unreversed[4:8]
)
spritesheet_bounding_boxes_asymmetric_reversed.extend(
    spritesheet_bounding_boxes_asymmetric_unreversed[0:4]
)

# pick the RHS block of sprites, I prefer drawing on that side :P
spritesheet_bounding_boxes_symmetric_unreversed = list(
    spritesheet_bounding_boxes_asymmetric_unreversed[4:8]
)
spritesheet_bounding_boxes_symmetric_unreversed.extend(
    spritesheet_bounding_boxes_asymmetric_unreversed[4:8]
)

# spritesheet_bounding_boxes_symmetric_reversed is identical to symmetric unreversed
# (reversing symmetrical vehicles is meaningless, but used for livery hax when some vehicles are flipped)
spritesheet_bounding_boxes_symmetric_reversed = (
    spritesheet_bounding_boxes_symmetric_unreversed
)

# rather than total spritesheet width, we often need to know the max x extent that actually contains sprites
# this is calculated from bounding boxes
sprites_max_x_extent = (
    spritesheet_bounding_boxes_asymmetric_unreversed[7][0]
    + spritesheet_bounding_boxes_asymmetric_unreversed[7][1]
)

# articulated parts must have a value less than 8192 (13 bit value)
max_articulated_id = 8191

# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# done this way so we don't have to pass Polar Fox to templates, we can just pass global_constants
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox.constants

base_refits_by_class = polar_fox.constants.base_refits_by_class
cargo_labels = polar_fox.constants.cargo_labels
chameleon_cache_dir = polar_fox.constants.chameleon_cache_dir
generated_files_dir = polar_fox.constants.generated_files_dir
mail_multiplier = polar_fox.constants.mail_multiplier
max_game_date = polar_fox.constants.max_game_date
company_colour_maps = polar_fox.constants.company_colour_maps
