# colour defaults
CC1 = 198
CC2 = 80

body_recolour_CC1 = {
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}
body_recolour_CC2 = {
    136: CC2,
    137: CC2 + 1,
    138: CC2 + 2,
    139: CC2 + 3,
    140: CC2 + 4,
    141: CC2 + 5,
    142: CC2 + 6,
    143: CC2 + 7,
}

# facts about 'standard' spritesheets, spritesheets varying from this will be painful
spriterow_height = 30
spritesheet_top_margin = 10
# wider than sprites, allows room for custom buy menu sprites, also to print cargo labels to aid drawing / debugging generated cargos
spritesheet_width = 425


# --- Body Recolour Maps --- #

tarpaulin_car_body_recolour_map = body_recolour_CC1

merchandise_car_body_recolour_map = {
    40: 4,
    41: 5,
    42: 6,
    43: 7,
    44: 20,
    45: 21,
    46: 22,
    47: 13,
}
merchandise_car_body_recolour_map_weathered = {
    40: 33,
    41: 34,
    42: 6,
    43: 36,
    44: 20,
    45: 21,
    46: 22,
    47: 39,
}

sliding_roof_car_body_recolour_map = {
    40: 4,
    41: 5,
    42: 6,
    43: 7,
    44: 20,
    45: 21,
    46: 22,
    47: 13,
}
sliding_roof_car_body_recolour_map_weathered = {
    40: 33,
    41: 34,
    42: 6,
    43: 36,
    44: 20,
    45: 21,
    46: 22,
    47: 39,
}

# --- Cargo Livery Recolour Maps --- #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah

# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
acid_tank_car_livery_recolour_maps = (
    (
        "DFLT",
        {
            136: CC1,
            137: CC1 + 1,
            138: CC1 + 2,
            139: CC1 + 3,
            140: CC1 + 4,
            141: CC1 + 5,
            142: CC1 + 6,
            143: CC1 + 7,
            154: CC1,
            155: CC1 + 1,
            156: CC1 + 2,
            157: CC1 + 3,
            158: CC1 + 4,
            159: CC1 + 5,
            160: CC1 + 6,
            161: CC1 + 7,
        },
    ),
    (
        "SULP",
        {
            136: 62,
            137: 62 + 1,
            138: 62 + 2,
            139: 62 + 3,
            140: 62 + 4,
            141: 62 + 5,
            142: 62 + 6,
            143: 62 + 7,
            154: 62,
            155: 62 + 1,
            156: 62 + 2,
            157: 62 + 3,
            158: 62 + 4,
            159: 62 + 5,
            160: 62 + 6,
            161: 62 + 7,
        },
    ),
)
acid_tank_car_livery_recolour_maps_weathered = (
    (
        "DFLT",
        {
            136: CC1,
            137: CC1 + 1,
            138: CC1 + 2,
            139: CC1 + 3,
            140: CC1 + 4,
            141: CC1 + 5,
            142: CC1 + 6,
            143: CC1 + 7,
            154: CC1,
            155: CC1 + 1,
            156: CC1 + 2,
            157: CC1 + 3,
            158: CC1 + 4,
            159: CC1 + 5,
            160: CC1 + 6,
            161: CC1 + 7,
        },
    ),
    (
        "SULP",
        {
            # should be kept in sync with the SULP map in polar fox tanker maps
            136: 62,
            137: 62 + 1,
            138: 62 + 2,
            139: 193,
            140: 194,
            141: 50,
            142: 51,
            143: 52,
            154: 62,
            155: 62 + 1,
            156: 62 + 2,
            157: 193,
            158: 194,
            159: 50,
            160: 51,
            161: 52,
        },
    ),
)

box_livery_recolour_maps = (
    (
        "DFLT",
        {
            136: CC1,
            137: CC1 + 1,
            138: CC1 + 2,
            139: CC1 + 3,
            140: CC1 + 4,
            141: CC1 + 5,
            142: CC1 + 6,
            143: CC1 + 7,
            40: CC1,
            41: CC1 + 1,
            42: CC1 + 2,
            43: CC1 + 3,
            44: CC1 + 4,
            45: CC1 + 5,
            46: CC1 + 6,
            47: CC1 + 7,
            CC2: CC1,
            CC2 + 1: CC1 + 1,
            CC2 + 2: CC1 + 2,
            CC2 + 3: CC1 + 3,
            CC2 + 4: CC1 + 4,
            CC2 + 5: CC1 + 5,
            CC2 + 6: CC1 + 6,
            CC2 + 7: CC1 + 7,
        },
    ),
)

caboose_livery_recolour_maps = (  # DFLT can be used twice here with no problems, it's not a unique key
    (
        "DFLT",
        {
            136: CC1,
            137: CC1 + 1,
            138: CC1 + 2,
            139: CC1 + 3,
            140: CC1 + 4,
            141: CC1 + 5,
            142: CC1 + 6,
            143: CC1 + 7,
            40: CC2,
            41: CC2 + 1,
            42: CC2 + 2,
            43: CC2 + 3,
            44: CC2 + 4,
            45: CC2 + 5,
            46: CC2 + 6,
            47: CC2 + 7,
        },
    ),
    (
        "DFLT",
        {
            136: CC2,
            137: CC2 + 1,
            138: CC2 + 2,
            139: CC2 + 3,
            140: CC2 + 4,
            141: CC2 + 5,
            142: CC2 + 6,
            143: CC2 + 7,
            40: CC1,
            41: CC1 + 1,
            42: CC1 + 2,
            43: CC1 + 3,
            44: CC1 + 4,
            45: CC1 + 5,
            46: CC1 + 6,
            47: CC1 + 7,
        },
    ),
)

carbon_black_hopper_car_livery_recolour_maps = (  # only one livery provided here, black
    (
        "DFLT",
        {
            136: 1,
            137: 2,
            138: 3,
            139: 4,
            140: 5,
            141: 6,
            142: 7,
            143: 8,
            154: 1,
            155: 2,
            156: 3,
            157: 4,
            158: 5,
            159: 6,
            160: 7,
            161: 8,
        },
    ),
)
carbon_black_hopper_car_livery_recolour_maps_weathered = (  # only one livery provided here, black
    (
        "DFLT",
        {
            136: 70,
            137: 1,
            138: 2,
            139: 3,
            140: 4,
            141: 5,
            142: 6,
            143: 19,
            154: 70,
            155: 1,
            156: 2,
            157: 3,
            158: 4,
            159: 5,
            160: 6,
            161: 19,
        },
    ),
)

cement_silo_livery_recolour_maps = (
    ("DFLT", {136: 53, 137: 54, 138: 6, 139: 57, 140: 30, 141: 38, 142: 13, 143: 15}),
)
cement_silo_livery_recolour_maps_weathered = (
    ("DFLT", {136: 53, 137: 4, 138: 35, 139: 36, 140: 10, 141: 59, 142: 13, 143: 15}),
)

chemical_covered_hopper_car_livery_recolour_maps = (
    (
        "DFLT",
        {
            136: 96,
            137: 54,
            138: 98,
            139: 56,
            140: 57,
            141: 58,
            142: 30,
            143: 197,
        },
    ),
)
chemical_covered_hopper_car_livery_recolour_maps_weathered = (
    (
        "DFLT",
        {
            136: 106,
            137: 33,
            138: 27,
            139: 35,
            140: 36,
            141: 37,
            142: 30,
            143: 168,
        },
    ),
)

covered_hopper_car_livery_recolour_maps = (
    (
        "DFLT",
        {
            136: CC1,
            137: CC1 + 1,
            138: CC1 + 2,
            139: CC1 + 3,
            140: CC1 + 4,
            141: CC1 + 5,
            142: CC1 + 6,
            143: CC1 + 7,
        },
    ),
)

curtain_side_livery_recolour_maps = (("DFLT", body_recolour_CC1),)

# pass through (recolour gestalt is used only to trigger automatic chassis drawing)
edibles_tank_car_livery_recolour_maps = (("DFLT", {}),)

farm_products_hopper_car_livery_recolour_maps = (
    (
        "DFLT",
        {136: 96, 137: 97, 138: 98, 139: 99, 140: 100, 141: 101, 142: 102, 143: 103},
    ),
)
farm_products_hopper_car_livery_recolour_maps_weathered = (
    (
        "DFLT",
        {136: 88, 137: 89, 138: 90, 139: 91, 140: 92, 141: 93, 142: 94, 143: 95},
    ),
)

farm_products_box_car_livery_recolour_maps = (
    (
        "DFLT",
        {
            136: 96,
            137: 96 + 1,
            138: 96 + 2,
            139: 96 + 3,
            140: 96 + 4,
            141: 96 + 5,
            142: 96 + 6,
            143: 96 + 7,
            40: 96,
            41: 96 + 1,
            42: 96 + 2,
            43: 96 + 3,
            44: 96 + 4,
            45: 96 + 5,
            46: 96 + 6,
            47: 96 + 7,
            CC1: 60,
            CC1 + 1: 60 + 1,
            CC1 + 2: 60 + 2,
            CC1 + 3: 60 + 3,
            CC1 + 4: 60 + 4,
            CC1 + 5: 60 + 5,
            CC1 + 6: 60 + 6,
            CC1 + 7: 60 + 7,
            CC2: 60,
            CC2 + 1: 60 + 1,
            CC2 + 2: 60 + 2,
            CC2 + 3: 60 + 3,
            CC2 + 4: 60 + 4,
            CC2 + 5: 60 + 5,
            CC2 + 6: 60 + 6,
            CC2 + 7: 60 + 7,
        },
    ),
)

kaolin_hopper_car_livery_recolour_maps = (
    (
        "DFLT",
        {
            # note that this very specifically recolours hand-drawn pixels to magic purple
            # this is to prevent these spriterows being incorrectly recoloured to 'weathered' due to the way the graphics pipeline works
            # these purple pixels are then reset to original when the weathered recolour map is applied
            17: 136,
            8: 139,
            12: 141,
            14: 142,
        },
    ),
)
kaolin_hopper_car_livery_recolour_maps_weathered = (
    (
        "DFLT",
        {
            17: 114,
            8: 36,
            12: 38,
            14: 39,
            # these are resets of magic purple applied by 'unweathered' map, back to original hand-drawn colours
            # order is significant, these must be applied after the 'weathered' remapping
            136: 17,
            139: 8,
            141: 12,
            142: 14,
        },
    ),
)

livestock_livery_recolour_maps = (("DFLT", body_recolour_CC2),)

mineral_covered_hopper_car_livery_recolour_maps = (
    (
        "DFLT",
        {
            # note that this very specifically recolours hand-drawn pixels to magic purple
            # this is to prevent these spriterows being incorrectly recoloured to 'weathered' due to the way the graphics pipeline works
            # these purple pixels are then reset to original when the weathered recolour map is applied
            18: 138,
            19: 139,
            22: 142,
        },
    ),
)
mineral_covered_hopper_car_livery_recolour_maps_weathered = (
    (
        "DFLT",
        {
            18: 115,
            19: 116,
            22: 120,
            # these are resets of magic purple applied by 'unweathered' map, back to original hand-drawn colours
            # order is significant, these must be applied after the 'weathered' remapping
            138: 18,
            139: 19,
            142: 22,
        },
    ),
)

oil_tank_car_livery_recolour_maps = (
    ("DFLT", {136: 1, 137: 2, 138: 3, 139: 4, 140: 5, 141: 6, 142: 7, 143: 8}),
)

pellet_hopper_car_livery_recolour_maps = (
    ("DFLT", {136: 4, 137: 5, 138: 6, 139: 19, 140: 20, 141: 21, 142: 22, 143: 23}),
)
pellet_hopper_car_livery_recolour_maps_weathered = (
    ("DFLT", {136: 33, 137: 5, 138: 6, 139: 8, 140: 9, 141: 21, 142: 22, 143: 23}),
)

product_tank_car_livery_recolour_maps = (
    ("DFLT", {136: 16, 137: 18, 138: 19, 139: 20, 140: 21, 141: 22, 142: 23, 143: 14}),
)
product_tank_car_livery_recolour_maps_weathered = (
    ("DFLT", {136: 16, 137: 5, 138: 7, 139: 9, 140: 10, 141: 22, 142: 23, 143: 14}),
)

refrigerated_livery_recolour_maps = (
    (
        "DFLT",
        {
            136: 18,
            137: 19,
            138: 20,
            139: 21,
            140: 22,
            141: 13,
            142: 14,
            143: 15,
            40: 18,
            41: 19,
            42: 20,
            43: 21,
            44: 22,
            45: 13,
            46: 14,
            47: 15,
            CC2: CC1,
            CC2 + 1: CC1 + 1,
            CC2 + 2: CC1 + 2,
            CC2 + 3: CC1 + 3,
            CC2 + 4: CC1 + 4,
            CC2 + 5: CC1 + 5,
            CC2 + 6: CC1 + 6,
            CC2 + 7: CC1 + 7,
        },
    ),
)

silo_livery_recolour_maps = (
    (
        "DFLT",
        {
            136: CC1,
            137: CC1 + 1,
            138: CC1 + 2,
            139: CC1 + 3,
            140: CC1 + 4,
            141: CC1 + 5,
            142: CC1 + 6,
            143: CC1 + 7,
        },
    ),
)

sliding_wall_livery_recolour_maps = (
    ("DFLT", {40: 4, 41: 5, 42: 6, 43: 7, 44: 20, 45: 21, 46: 22, 47: 13}),
)
sliding_wall_livery_recolour_maps_weathered = (
    ("DFLT", {40: 33, 41: 34, 42: 6, 43: 36, 44: 20, 45: 21, 46: 22, 47: 39}),
)
