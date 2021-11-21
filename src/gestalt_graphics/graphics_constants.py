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

cement_silo_livery_recolour_maps = (
    ("DFLT", {136: 53, 137: 54, 138: 6, 139: 57, 140: 30, 141: 38, 142: 13, 143: 15}),
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

# ideally this would also randomise to 88-95, not sure how to do that as of Nov 2021
farm_products_hopper_car_livery_recolour_maps = (("DFLT", {136: 96, 137: 97, 138: 98, 139: 99, 140: 100, 141: 101, 142: 102, 143: 103}),)

fruit_veg_livery_recolour_maps = (
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
            40: 71,
            41: 72,
            42: 73,
            43: 74,
            44: 75,
            45: 77,
            46: 78,
            47: 79,
            CC1: 71,
            CC1 + 1: 72,
            CC1 + 2: 73,
            CC1 + 3: 74,
            CC1 + 4: 75,
            CC1 + 5: 77,
            CC1 + 6: 78,
            CC1 + 7: 79,
        },
    ),
)

livestock_livery_recolour_maps = (("DFLT", body_recolour_CC2),)

oil_tank_car_livery_recolour_maps = (
    ("DFLT", {136: 1, 137: 2, 138: 3, 139: 4, 140: 5, 141: 6, 142: 7, 143: 8}),
)

pellet_hopper_car_livery_recolour_maps = (
    ("DFLT", {136: 16, 137: 17, 138: 18, 139: 19, 140: 20, 141: 21, 142: 22, 143: 23}),
)

potash_hopper_car_livery_recolour_maps = (  # only one livery provided here, black
    (
        "DFLT",
        {
            136: 53,
            137: 54,
            138: 98,
            139: 56,
            140: 57,
            141: 58,
            142: 30,
            143: 196,
        },
    ),
)

product_tank_car_livery_recolour_maps = (
    ("DFLT", {136: 16, 137: 18, 138: 19, 139: 20, 140: 21, 141: 22, 142: 23, 143: 14}),
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
