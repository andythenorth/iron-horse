from collections import OrderedDict

# list in buy menu order
wagon_module_names = [
    # """
    # # only comment in if needed for debugging
    # "alignment_cars",
    # """
    "hst_passenger_cars",
    "hst_mail_cars",
    "railbus_passenger_trailer_cars",
    "railcar_passenger_trailer_cars",
    "express_railcar_mail_trailer_cars",
    "express_railcar_passenger_trailer_cars",
    "passenger_cars",
    "panoramic_cars",
    "high_speed_passenger_cars",
    "restaurant_cars",
    "suburban_passenger_cars",
    "mail_cars",
    "high_speed_mail_cars",
    "express_cars",
    "enclosed_automobile_cars",
    "automobile_cars",
    # "low_floor_automobile_cars",
    "double_deck_automobile_cars",  # order before other automobile cars as needed in simplified mode
    "express_intermodal_cars",
    "intermodal_cars",
    "low_floor_intermodal_cars",
    "open_cars",
    "merchandise_open_cars",
    "hood_open_cars",
    "randomised_open_cars",
    "box_cars",
    "merchandise_box_cars",
    "curtain_side_box_cars",
    "randomised_box_cars",
    "sliding_wall_cars",
    "vehicle_parts_box_cars",
    "goods_box_cars",
    "plate_cars",
    "flat_cars",
    "bulkhead_flat_cars",
    "sliding_roof_cars",
    "sliding_roof_hi_cube_cars",
    "tarpaulin_cars",
    "bolster_cars",
    "coil_cars_covered",
    "coil_cars_covered_asymmetric",
    "coil_cars_uncovered",
    "randomised_dedicated_coil_cars",
    "hopper_cars",
    "hopper_cars_high_side",
    "aggregate_hopper_cars_type_1",
    "aggregate_hopper_cars_type_2",
    "aggregate_hopper_cars_type_3",
    "randomised_aggregate_hopper_cars",
    "rock_hopper_cars",
    "mgr_hopper_cars",
    "mgr_hopper_top_hood_cars",
    "dump_cars",
    "dump_cars_high_side",
    "randomised_dump_cars",
    "aggregate_dump_cars_type_1",
    "aggregate_dump_cars_type_2",
    "aggregate_dump_cars_type_3",
    "aggregate_dump_cars_type_4",
    "aggregate_dump_cars_type_5",
    "aggregate_dump_cars_type_6",
    "randomised_aggregate_dump_cars",
    "ore_dump_cars",
    "scrap_metal_cars",
    "skip_cars",
    "tank_cars",
    "product_tank_cars",
    "sulphur_tank_cars",
    "acid_tank_cars",
    "pressure_tank_cars",
    "cryo_tank_cars",
    "covered_hopper_cars",
    "dry_powder_hopper_cars",
    "mineral_covered_hopper_cars",
    "chemical_covered_hopper_cars",
    "roller_roof_hopper_cars",
    "swing_roof_hopper_cars",
    "silo_cars",
    "silo_cars_v_barrel",
    "randomised_silo_cars",
    "cement_silo_cars",
    "cement_silo_cars_v_barrel",
    "randomised_cement_silo_cars",
    "livestock_cars",
    "edibles_tank_cars",
    "reefer_cars_type_1",
    "reefer_cars_type_2",
    "farm_products_box_cars",
    "farm_products_hopper_cars_type_1",
    "farm_products_hopper_cars_type_2",
    "randomised_farm_products_hopper_cars",
    "log_cars",
    "kaolin_hopper_cars",
    "carbon_black_hopper_cars",
    "peat_cars",
    # "well_cars",
    "torpedo_cars",
    "coil_buggy_cars",
    "ingot_cars",
    "slag_ladle_cars",
    "heavy_duty_dump_cars",
    "heavy_duty_flat_cars",
    "randomised_piece_goods_cars",
    "randomised_flat_cars",
    "randomised_generic_coil_cars",
    "randomised_hopper_cars",
    "randomised_bulk_cars",
    "randomised_chemicals_tank_cars",
    "randomised_covered_hopper_cars",
    "caboose_cars",
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
    "RAIL_ELECTRIFIED_DC": ["IHF_"],  # no fallback for DC if not present
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
            ["universal"],
        ),
        # railcars get their own special cases due to high capacity, bit janky but eh
        (
            "suburban_or_universal_railcar",
            ["pax_railbus", "pax_railcar", "pax_suburban_coach"],
        ),
        (
            "mail_railcar",
            ["mail_railcar"],
        ),
        ("express_railcar", ["express_pax_railcar", "express_mail_railcar"]),
        ("hst", ["hst"]),
        ("very_high_speed", ["very_high_speed"]),
        (
            "driving_cab",
            [
                "driving_cab_express_pax",
                "driving_cab_express_mail",
                "driving_cab_express_mixed",
            ],
        ),
        (
            "gronk!",
            [
                "gronk!",
            ],
        ),
        (
            "lolz",
            [
                "snoughplough!",
            ],
        ),
        ("metro", ["pax_metro", "mail_metro", "metro"]),  # note pax before mail
    ]
)

# keep alphabetised, order not significant
role_string_mapping = {
    "driving_cab": "STR_ROLE_DRIVING_CAB",
    "express": "STR_ROLE_GENERAL_PURPOSE_EXPRESS",
    "express_railcar": "STR_ROLE_GENERAL_PURPOSE_EXPRESS",
    "freight": "STR_ROLE_GENERAL_PURPOSE_FREIGHT",
    "gronk!": "STR_ROLE_GRONK",
    "high_power_railcar": "STR_ROLE_GENERAL_PURPOSE_EXPRESS",
    "hst": "STR_ROLE_INTERCITY_EXPRESS",
    "lolz": "STR_ROLE_LOLZ",
    "mail_railcar": "STR_ROLE_GENERAL_PURPOSE",
    "metro": "STR_ROLE_METRO",
    "suburban_or_universal_railcar": "STR_ROLE_SUBURBAN",
    "universal": "STR_ROLE_GENERAL_PURPOSE",
    "very_high_speed": "STR_ROLE_INTERCITY_EXPRESS",
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
    "suburban_or_universal_railcar": 6,
    "mail_railcar": 6,
    "metro": 7,
    "very_high_speed": 8,
    "food_wagons": 9,
    "non_core_wagons": 10,
    "gronk!": 11,
    "lolz": 11,
}

# shared across all rosters, keep alphabetised, order not significant
# only needed for groups composing more than one type of consist
buyable_variant_group_consist_base_ids_by_group_name = {
    "wagon_group_acid_tank_cars": "acid_tank_car",
    "wagon_group_aggregate_dump_cars": "aggregate_dump_car_type_1",
    "wagon_group_aggregate_hopper_cars": "aggregate_hopper_car_type_1",
    "wagon_group_box_cars": "box_car",
    "wagon_group_cement_silo_cars": "cement_silo_car",
    "wagon_group_coil_cars": "coil_car_uncovered",
    "wagon_group_covered_hopper_cars": "covered_hopper_car",
    "wagon_group_dump_cars": "dump_car",
    "wagon_group_farm_product_cars": "farm_products_hopper_car_type_1",
    "wagon_group_hopper_cars": "hopper_car",
    "wagon_group_mgr_hopper_cars": "mgr_hopper_car",
    "wagon_group_intermodal_cars": "intermodal_car",
    "wagon_group_open_cars": "open_car",
    "wagon_group_passenger_cars": "passenger_car",
    "wagon_group_pressure_tank_cars": "pressure_tank_car",
    "wagon_group_reefer_cars": "reefer_car_type_1",
    "wagon_group_silo_cars": "silo_car",
    "wagon_group_sliding_wall_cars": "sliding_wall_car",
    "wagon_group_vehicle_transporter_cars": "automobile_car",
}

# custom remappings of cc1/cc2, used in recolour_sprites, not used in graphics generation, so not in graphics_constants
# post python 3.7, we rely on dict order being stable here, so we can get keys by position when we need to
custom_wagon_recolour_sprite_maps = {
    "custom_dark_brown": (105, 106, 33, 34, 35, 36, 37, 38),
    "custom_dark_pink": (40, 41, 42, 43, 44, 45, 46, 47),
    "custom_light_pink": (43, 44, 45, 46, 47, 166, 167, 168),
    "custom_dark_grey": (3, 16, 17, 18, 19, 20, 21, 22),
    "custom_dark_yellow": (60, 61, 62, 64, 65, 66, 67, 68),
    "custom_dark_white": (18, 7, 8, 10, 11, 12, 13, 14),
    "custom_light_purple": (136, 170, 171, 172, 173, 174, 175, 176),
    "custom_light_mauve": (129, 130, 131, 132, 133, 134, 135, 14),
    "custom_dark_orange": (62, 63, 64, 193, 194, 195, 196, 197),
    "custom_dark_cream": (112, 113, 114, 116, 117, 118, 119, 120),
    # can't name it dark_green cos that conflates with DARK_GREEN
    "custom_green": (
        80,
        82,
        83,
        84,
        85,
        86,
        207,
        209,
    ),
    # can't name it dark_blue cos that conflates with DARK_BLUE
    "custom_blue": (
        147,
        148,
        149,
        150,
        151,
        152,
        153,
        210,
    ),
    # can't name it dark_light_blue cos that would be silly
    "custom_light_blue": (
        155,
        156,
        157,
        158,
        159,
        160,
        161,
        210,
    ),
    # can't name it light_dark_blue cos that would be silly
    "custom_dark_blue": (
        199,
        200,
        201,
        202,
        203,
        204,
        205,
        152,
    ),
    "custom_dark_red": (180, 181, 182, 183, 164, 165, 166, 167),
    "custom_pale_green": (97, 98, 99, 100, 101, 102, 103, 14),
    "custom_dark_green": (89, 90, 91, 92, 93, 94, 95, 31),
    # tried darker bauxite colours, doesn't work well
    "custom_bauxite": (70, 71, 122, 124, 75, 126, 77, 78),
    "custom_light_bauxite": (71, 122, 74, 125, 76, 127, 78, 79),
    "custom_nightshade": (104, 2, 25, 17, 18, 19, 20, 10),
    "custom_light_nightshade": (1, 2, 106, 17, 18, 7, 20, 10),
    "custom_teal": (88, 97, 98, 157, 158, 159, 160, 103),
    "custom_dark_teal": (88, 97, 156, 157, 158, 101, 102, 103),
    "custom_violet": (136, 170, 171, 172, 173, 174, 175, 176),  # WIP, may need improved
    "custom_dark_violet": (
        129,
        130,
        131,
        132,
        133,
        134,
        135,
        14,
    ),  # WIP, may need improved
    "custom_silver": (2, 18, 19, 20, 21, 22, 23, 14),
    "custom_dark_silver": (2, 4, 35, 19, 21, 22, 23, 14),
    "custom_pewter": (2, 3, 18, 19, 20, 21, 22, 13),
    "custom_dark_pewter": (2, 114, 18, 19, 20, 21, 22, 13),
    "custom_sulphur": (62, 62 + 1, 62 + 2, 62 + 3, 62 + 4, 62 + 5, 62 + 6, 62 + 7),
    "custom_dark_sulphur": (62, 62 + 1, 62 + 2, 193, 194, 50, 51, 52),
    "custom_ruby": (40, 41, 42, 43, 44, 45, 46, 47),
    "custom_faded_ruby": (71, 72, 73, 43, 44, 76, 77, 47),
    "custom_oil_black": (1, 2, 3, 4, 5, 6, 7, 8),
    "custom_faded_oil_black": (1, 70, 16, 4, 26, 6, 7, 8),
    "custom_gremlin_green": (24, 25, 26, 27, 28, 29, 30, 31),
    "custom_faded_gremlin_green": (24, 25, 26, 109, 28, 29, 59, 103),
    "custom_ochre": (60, 61, 62, 63, 192, 193, 194, 196),
    "custom_faded_ochre": (60, 61, 62, 117, 192, 193, 196, 197),
}

# shared colour sets with variants of CC, may be used by multiple strategies, not used in graphics generation, so not in graphics_constants
# post python 3.7, we rely on dict order being stable here, so we can get keys by position when we need to
colour_sets = {
    "dark_blue": ["COLOUR_DARK_BLUE", "custom_dark_blue"],
    "pale_green": ["COLOUR_PALE_GREEN", "custom_pale_green"],
    "pink": ["COLOUR_PINK", "custom_dark_pink"],
    "yellow": ["COLOUR_YELLOW", "custom_dark_yellow"],
    "red": ["COLOUR_RED", "custom_dark_red"],
    "light_blue": ["COLOUR_LIGHT_BLUE", "custom_light_blue"],
    "green": ["COLOUR_GREEN", "custom_green"],
    "dark_green": ["COLOUR_DARK_GREEN", "custom_dark_green"],
    "blue": ["COLOUR_BLUE", "custom_blue"],
    "cream": ["COLOUR_CREAM", "custom_dark_cream"],
    "mauve": ["COLOUR_MAUVE", "custom_light_mauve"],
    "purple": ["COLOUR_PURPLE", "custom_light_purple"],
    "orange": ["COLOUR_ORANGE", "custom_dark_orange"],
    "brown": ["COLOUR_BROWN", "custom_dark_brown"],
    "grey": ["COLOUR_GREY", "custom_dark_grey"],
    "white": ["COLOUR_WHITE", "custom_dark_white"],
    "freight_bauxite": ["custom_bauxite", "custom_light_bauxite"],
    "freight_grey": ["custom_dark_grey", "COLOUR_GREY"],
    "freight_nightshade": ["custom_nightshade", "custom_light_nightshade"],
    "freight_teal": ["custom_teal", "custom_dark_teal"],
    "freight_violet": ["custom_violet", "custom_dark_violet"],
    "freight_silver": ["custom_silver", "custom_dark_silver"],
    "freight_pewter": ["custom_pewter", "custom_dark_pewter"],
    "freight_sulphur": ["custom_sulphur", "custom_dark_sulphur"],
    "freight_straw": ["COLOUR_BROWN", "COLOUR_CREAM"],
    "freight_ruby": ["custom_ruby", "custom_faded_ruby"],
    "freight_oil_black": ["custom_oil_black", "custom_faded_oil_black"],
    "freight_gremlin_green": ["custom_gremlin_green", "custom_faded_gremlin_green"],
    "freight_ochre": ["custom_ochre", "custom_faded_ochre"],
    "freight_sand": ["COLOUR_BROWN", "custom_dark_brown"],
}

# select a colour that matches the current company colour
# current company colour: complementary colour
complements_to_company_colours = {
    "COLOUR_DARK_BLUE": "COLOUR_BLUE",
    "COLOUR_PALE_GREEN": "COLOUR_GREEN",
    "COLOUR_PINK": "COLOUR_RED",
    "COLOUR_YELLOW": "COLOUR_ORANGE",
    "COLOUR_RED": "COLOUR_PINK",
    "COLOUR_LIGHT_BLUE": "COLOUR_BLUE",
    "COLOUR_GREEN": "COLOUR_DARK_GREEN",
    "COLOUR_DARK_GREEN": "COLOUR_GREEN",
    "COLOUR_BLUE": "COLOUR_DARK_BLUE",
    "COLOUR_CREAM": "COLOUR_BROWN",
    "COLOUR_MAUVE": "COLOUR_PURPLE",
    "COLOUR_PURPLE": "COLOUR_MAUVE",
    "COLOUR_ORANGE": "COLOUR_YELLOW",
    "COLOUR_BROWN": "COLOUR_CREAM",
    "COLOUR_GREY": "COLOUR_BROWN",  # more likely we want to complement grey with brown than white
    "COLOUR_WHITE": "COLOUR_GREY",
}

# wagon liveries overlap between rosters so are in global constants (engine liveries are per-roster)
# custom remappings of cc1/cc2, used in recolour_sprites, not used in graphics generation, so not in graphics_constants
freight_wagon_liveries = {
    # SWOOSH is default, and only used for cases where the livery isn't actually meaningful, e.g. randomised consists
    "SWOOSH": {
        "colour_set": "company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "COMPANY_COLOUR_USE_WEATHERING": {
        "colour_set": "company_colour",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "COMPANY_COLOUR_NO_WEATHERING": {
        "colour_set": "company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "COMPLEMENT_COMPANY_COLOUR_USE_WEATHERING": {
        "colour_set": "complement_company_colour",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "COMPLEMENT_COMPANY_COLOUR_NO_WEATHERING": {
        "colour_set": "complement_company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_1": {
        "colour_set": "random_from_consist_liveries_1",
        "purchase": "company_colour",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_NO_WEATHERING_1": {
        "colour_set": "random_from_consist_liveries_1",
        "purchase": "company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_2": {
        "colour_set": "random_from_consist_liveries_2",
        "purchase": "complement_company_colour",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_NO_WEATHERING_2": {
        "colour_set": "random_from_consist_liveries_2",
        "purchase": "complement_company_colour",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_3": {
        "colour_set": "random_from_consist_liveries_3",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_NO_WEATHERING_3": {
        "colour_set": "random_from_consist_liveries_3",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_4": {
        "colour_set": "random_from_consist_liveries_4",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_5": {
        "colour_set": "random_from_consist_liveries_5",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_6": {
        "colour_set": "random_from_consist_liveries_6",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_7": {
        "colour_set": "random_from_consist_liveries_7",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_8": {
        "colour_set": "random_from_consist_liveries_8",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_9": {
        "colour_set": "random_from_consist_liveries_9",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_10": {
        "colour_set": "random_from_consist_liveries_10",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "RANDOM_FROM_CONSIST_LIVERIES_11": {
        "colour_set": "random_from_consist_liveries_11",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_BAUXITE": {
        "colour_set": "freight_bauxite",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_BAUXITE_NO_WEATHERING": {
        "colour_set": "freight_bauxite",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_GREMLIN_GREEN": {
        "colour_set": "freight_gremlin_green",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_GREY": {
        "colour_set": "freight_grey",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_GREY_NO_WEATHERING": {
        "colour_set": "freight_grey",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_NIGHTSHADE": {
        "colour_set": "freight_nightshade",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_NIGHTSHADE_NO_WEATHERING": {
        "colour_set": "freight_nightshade",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_OCHRE": {
        "colour_set": "freight_ochre",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_OIL_BLACK": {
        "colour_set": "freight_oil_black",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_PEWTER": {
        "colour_set": "freight_pewter",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_RUBY": {
        "colour_set": "freight_ruby",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_RED": {
        "colour_set": "red",
        "use_weathering": False,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_SAND": {
        "colour_set": "freight_sand",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_SILVER": {
        "colour_set": "freight_silver",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_STRAW": {
        "colour_set": "freight_straw",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_SULPHUR": {
        "colour_set": "freight_sulphur",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_TEAL": {
        "colour_set": "freight_teal",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "FREIGHT_VIOLET": {
        "colour_set": "freight_violet",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "CC_BLUE": {
        "colour_set": "blue",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
    "CC_DARK_BLUE": {
        "colour_set": "dark_blue",
        "use_weathering": True,
        "docs_image_input_cc": [
            ("COLOUR_BLUE", "COLOUR_BLUE"),
            ("COLOUR_RED", "COLOUR_WHITE"),
        ],
    },
}

# for wagons with mixed livery, the permitted liveries for that specific mix type
wagon_livery_mixes = {
    # company colour + 1
    "random_from_consist_liveries_1": ["complement_company_colour", "company_colour"],
    # most everything (but explicit add, so not *everything*)
    "random_from_consist_liveries_2": [
        "company_colour",
        "complement_company_colour",
        "freight_bauxite",
        "freight_grey",
        "freight_nightshade",
        "freight_silver",
        "freight_teal",
        "freight_violet",
    ],
    # rust belt
    "random_from_consist_liveries_3": [
        "freight_bauxite",
        "freight_grey",
        "freight_nightshade",
    ],
    # chemicals
    "random_from_consist_liveries_4": ["freight_teal", "freight_violet"],
    # silver-ish
    "random_from_consist_liveries_5": ["freight_silver", "freight_pewter"],
    # yellow / ochre
    "random_from_consist_liveries_6": ["freight_sulphur", "freight_ochre"],
    # rust / ruby
    "random_from_consist_liveries_7": ["freight_ruby", "freight_bauxite"],
    # black
    "random_from_consist_liveries_8": ["freight_oil_black", "freight_nightshade"],
    # ochre / sand
    "random_from_consist_liveries_9": ["freight_ochre", "freight_sand"],
    # moss /
    "random_from_consist_liveries_10": ["freight_gremlin_green", "freight_silver"],
    # yellow / faded
    "random_from_consist_liveries_11": ["freight_sulphur", "freight_straw"],
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
    cc_num_to_recolour=20,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_strategy_num=21,  # used in procedures_wagon_recolour_strategies
    unreversible_spritelayer_cargos=22,  # used to handle esoteric cases where spritelayer cargos need to reverse
    consist_specific_position_variant_num=23,  # used to store result of switch_graphics_pax_car_ruleset() and similar
    flag_use_weathering=24,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_livery_num_0=25,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_livery_num_1=26,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_livery_num_2=27,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_livery_num_3=28,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_livery_num_4=29,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_livery_num_5=30,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_livery_num_6=31,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_livery_num_7=32,  # used in procedures_wagon_recolour_strategies
    flag_context_is_purchase=33,  # used in procedures_wagon_recolour_strategies
    wagon_recolour_strategy_num_purchase=34,  # used in procedures_wagon_recolour_strategies
    position_in_vehid_chain_base_offset=35,  # used in position rulesets, an offset into position_in_vehid_chain_multiple_ids
    position_in_vehid_chain_multiple_ids_with_base_offset_applied=36,  # position_in_vehid_chain_multiple_ids, with a base offset applied
    name_substr_default_name_1=37,  # name substring
    name_substr_default_name_2=38,  # name substring
    name_substr_default_name_3=39,  # name substring
    name_substr_default_name_4=40,  # name substring
    name_substr_purchase_level_0_1=41,  # name substring
    name_substr_purchase_level_0_2=42,  # name substring
    name_substr_purchase_level_0_3=43,  # name substring
    name_substr_purchase_level_0_4=44,  # name substring
    name_substr_purchase_level_1_1=45,  # name substring
    name_substr_purchase_level_1_2=46,  # name substring
    name_substr_purchase_level_1_3=47,  # name substring
    name_substr_purchase_level_1_4=48,  # name substring
    name_substr_purchase_level_1_5=49,  # name substring
    name_substr_purchase_level_1_6=50,  # name substring
    name_substr_autoreplace_lhs_1=51,  # name substring
    name_substr_autoreplace_lhs_2=52,  # name substring
    name_substr_autoreplace_lhs_3=53,  # name substring
    name_substr_autoreplace_lhs_4=54,  # name substring
    name_substr_autoreplace_lhs_5=55,  # name substring
    name_substr_autoreplace_lhs_6=56,  # name substring
    name_substr_from_property=57,  # name substring
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

# rather than total spritesheet width, we often need to know the max x extent that actually contains sprites
# this is calculated from bounding boxes
sprites_max_x_extent = (
    spritesheet_bounding_boxes_asymmetric_unreversed[7][0]
    + spritesheet_bounding_boxes_asymmetric_unreversed[7][1]
)

# articulated parts must have an ID less than 16383 (13 bit value)
max_articulated_id = 16383

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
