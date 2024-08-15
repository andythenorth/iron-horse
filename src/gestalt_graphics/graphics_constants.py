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

# overlay items for randomised wagons
dice_image_width = 14
randomised_wagon_extra_unit_width = 4

# --- Body Recolour Maps --- #

tarpaulin_car_body_recolour_map = body_recolour_CC1

caboose_car_body_recolour_map = {
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}

coil_car_tarpaulin_body_recolour_map = {
    40: 2,
    41: 128,
    42: 129,
    43: 5,
    44: 18,
    45: 19,
    46: 20,
    47: 10,
}
coil_car_tarpaulin_body_recolour_map_weathered = {
    40: 106,
    41: 33,
    42: 130,
    43: 35,
    44: 19,
    45: 20,
    46: 21,
    47: 38,
}

hood_open_car_body_recolour_map = {
    136: 71,
    136 + 1: 72,
    136 + 2: 73,
    136 + 3: 74,
    136 + 4: 75,
    136 + 5: 76,
    136 + 6: 77,
    136 + 7: 118,
}
hood_open_car_body_recolour_map_weathered = {
    136: 71,
    136 + 1: 72,
    136 + 2: 73,
    136 + 3: 114,
    136 + 4: 115,
    136 + 5: 116,
    136 + 6: 117,
    136 + 7: 118,
}

box_car_type_2_body_recolour_map = {
    40: 4,
    40 + 1: 5,
    40 + 2: 6,
    40 + 3: 7,
    40 + 4: 20,
    40 + 5: 21,
    40 + 6: 22,
    40 + 7: 13,
    136: 4,
    136 + 1: 5,
    136 + 2: 6,
    136 + 3: 7,
    136 + 4: 20,
    136 + 5: 21,
    136 + 6: 22,
    136 + 7: 13,
}
box_car_type_2_body_recolour_map_weathered = {
    40: 33,
    40 + 1: 34,
    40 + 2: 6,
    40 + 3: 36,
    40 + 4: 20,
    40 + 5: 21,
    40 + 6: 22,
    40 + 7: 39,
    136: 33,
    136 + 1: 34,
    136 + 2: 6,
    136 + 3: 36,
    136 + 4: 20,
    136 + 5: 21,
    136 + 6: 22,
    136 + 7: 39,
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

# --- Simple Body Colour Recolour Maps --- #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah
acid_tank_car_type_2_livery_recolour_maps = {
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
}
acid_tank_car_type_2_livery_recolour_maps_weathered = {
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
}
box_livery_recolour_maps = {
    40: CC1,
    41: CC1 + 1,
    42: CC1 + 2,
    43: CC1 + 3,
    44: CC1 + 4,
    45: CC1 + 5,
    46: CC1 + 6,
    47: CC1 + 7,
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}
carbon_black_hopper_car_livery_recolour_maps = {
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
}
carbon_black_hopper_car_livery_recolour_maps_weathered = {
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
}
cement_silo_livery_recolour_maps = {
    136: 53,
    137: 54,
    138: 6,
    139: 57,
    140: 30,
    141: 38,
    142: 13,
    143: 15,
}
cement_silo_livery_recolour_maps_weathered = {
    136: 53,
    137: 4,
    138: 35,
    139: 36,
    140: 10,
    141: 59,
    142: 13,
    143: 15,
}

chemical_covered_hopper_car_livery_recolour_maps = {
    136: 96,
    137: 54,
    138: 98,
    139: 56,
    140: 57,
    141: 58,
    142: 30,
    143: 197,
}
chemical_covered_hopper_car_livery_recolour_maps_weathered = {
    136: 106,
    137: 33,
    138: 27,
    139: 35,
    140: 36,
    141: 37,
    142: 30,
    143: 168,
}
covered_coil_car_asymmetric_body_recolour_map = {
    136: 5,
    137: 6,
    138: 7,
    139: 20,
    140: 21,
    141: 22,
    142: 23,
    143: 14,
}
covered_coil_car_asymmetric_body_recolour_map_weathered = {
    136: 33,
    137: 34,
    138: 7,
    139: 36,
    140: 21,
    141: 22,
    142: 23,
    143: 39,
}
v_barrel_silo_car_livery_recolour_maps = {
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}
covered_hopper_car_livery_recolour_maps = {
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}
# broken away from Polar Fox, as the automatic chlorine cargo recolour is dropped for these as of August 2023
cryo_tanker_livery_recolour_maps = {
    136: 5,
    137: 7,
    138: 9,
    139: 11,
    140: 12,
    141: 13,
    142: 14,
    143: 15,
}
cryo_tanker_livery_recolour_maps_weathered = {
    136: 34,
    137: 7,
    138: 9,
    139: 11,
    140: 12,
    141: 38,
    142: 14,
    143: 15,
}

curtain_side_livery_recolour_maps = body_recolour_CC1

# pass through (recolour gestalt is used only to trigger automatic chassis drawing)
food_tank_car_livery_recolour_maps = {}

farm_product_hopper_car_livery_recolour_maps = {
    136: 96,
    137: 97,
    138: 98,
    139: 99,
    140: 100,
    141: 101,
    142: 102,
    143: 103,
}
farm_product_hopper_car_livery_recolour_maps_weathered = {
    136: 88,
    137: 89,
    138: 90,
    139: 91,
    140: 92,
    141: 93,
    142: 94,
    143: 95,
}

farm_product_box_car_livery_recolour_maps = {
    40: 96,
    41: 96 + 1,
    42: 96 + 2,
    43: 96 + 3,
    44: 96 + 4,
    45: 96 + 5,
    46: 96 + 6,
    47: 96 + 7,
    CC1: 61,
    CC1 + 1: 61 + 1,
    CC1 + 2: 61 + 2,
    CC1 + 3: 61 + 3,
    CC1 + 4: 61 + 4,
    CC1 + 5: 61 + 5,
    CC1 + 6: 61 + 6,
    CC1 + 7: 61 + 7,
}
farm_product_box_car_livery_recolour_maps_weathered = {
    40: 88,
    41: 88 + 1,
    42: 88 + 2,
    43: 88 + 3,
    44: 88 + 4,
    45: 88 + 5,
    46: 88 + 6,
    47: 88 + 7,
    CC1: 61,
    CC1 + 1: 61 + 1,
    CC1 + 2: 61 + 2,
    CC1 + 3: 61 + 3,
    CC1 + 4: 61 + 4,
    CC1 + 5: 61 + 5,
    CC1 + 6: 61 + 6,
    CC1 + 7: 61 + 7,
}
merchandise_box_car_body_recolour_maps = {
    136: 70,
    136 + 1: 71,
    136 + 2: 72,
    136 + 3: 73,
    136 + 4: 74,
    136 + 5: 75,
    136 + 6: 76,
    136 + 7: 118,
}
merchandise_box_car_body_recolour_maps_weathered = {
    136: 70,
    136 + 1: 71,
    136 + 2: 72,
    136 + 3: 113,
    136 + 4: 114,
    136 + 5: 115,
    136 + 6: 116,
    136 + 7: 118,
}
kaolin_hopper_car_livery_recolour_maps = {
    # note that this very specifically recolours hand-drawn pixels to magic purple
    # this is to prevent these spriterows being incorrectly recoloured to 'weathered' due to the way the graphics pipeline works
    # these purple pixels are then reset to original when the weathered recolour map is applied
    17: 136,
    8: 139,
    12: 141,
    14: 142,
}
kaolin_hopper_car_livery_recolour_maps_weathered = {
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
}
livestock_livery_recolour_maps = body_recolour_CC1

mineral_covered_hopper_car_livery_recolour_maps = {
    # note that this very specifically recolours hand-drawn pixels to magic purple
    # this is to prevent these spriterows being incorrectly recoloured to 'weathered' due to the way the graphics pipeline works
    # these purple pixels are then reset to original when the weathered recolour map is applied
    18: 138,
    19: 139,
    22: 142,
}
mineral_covered_hopper_car_livery_recolour_maps_weathered = {
    18: 115,
    19: 116,
    22: 120,
    # these are resets of magic purple applied by 'unweathered' map, back to original hand-drawn colours
    # order is significant, these must be applied after the 'weathered' remapping
    138: 18,
    139: 19,
    142: 22,
}
pellet_hopper_car_livery_recolour_maps = {
    136: 4,
    137: 5,
    138: 6,
    139: 19,
    140: 20,
    141: 21,
    142: 22,
    143: 23,
}
pellet_hopper_car_livery_recolour_maps_weathered = {
    136: 33,
    137: 5,
    138: 6,
    139: 8,
    140: 9,
    141: 21,
    142: 22,
    143: 23,
}

product_tank_car_livery_recolour_maps = {
    136: 16,
    137: 18,
    138: 19,
    139: 20,
    140: 21,
    141: 22,
    142: 23,
    143: 14,
}
product_tank_car_livery_recolour_maps_weathered = {
    136: 16,
    137: 5,
    138: 7,
    139: 9,
    140: 10,
    141: 22,
    142: 23,
    143: 14,
}

refrigerated_livery_recolour_maps = {
    136: 18,
    137: 19,
    138: 20,
    139: 21,
    140: 22,
    141: 13,
    142: 14,
    143: 15,
}
refrigerated_livery_recolour_maps_weathered = {
    136: 17,
    137: 18,
    138: 19,
    139: 20,
    140: 21,
    141: 12,
    142: 13,
    143: 15,
}
silo_livery_recolour_maps = {
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}
sliding_wall_livery_recolour_maps = {
    40: 4,
    41: 5,
    42: 6,
    43: 7,
    44: 20,
    45: 21,
    46: 22,
    47: 13,
}
sliding_wall_livery_recolour_maps_weathered = {
    40: 33,
    41: 34,
    42: 6,
    43: 36,
    44: 20,
    45: 21,
    46: 22,
    47: 39,
}

acid_tank_car_type_1_livery_recolour_maps = {
    136: 104,
    137: 2,
    138: 25,
    139: 17,
    140: 18,
    141: 19,
    142: 20,
    143: 10,
    154: CC1,
    155: CC1 + 1,
    156: CC1 + 2,
    157: CC1 + 3,
    158: CC1 + 4,
    159: CC1 + 5,
    160: CC1 + 6,
    161: CC1 + 7,
}
acid_tank_car_type_1_livery_recolour_maps_weathered = {
    # should be kept in sync with the SULP map in polar fox tanker maps
    136: 1,
    137: 2,
    138: 106,
    139: 17,
    140: 18,
    141: 7,
    142: 20,
    143: 10,
    154: CC1,
    155: CC1 + 1,
    156: CC1 + 2,
    157: CC1 + 3,
    158: CC1 + 4,
    159: CC1 + 5,
    160: CC1 + 6,
    161: CC1 + 7,
}
tank_car_livery_recolour_maps = {
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}
