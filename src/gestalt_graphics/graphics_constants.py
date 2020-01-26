# colour defaults
CC1 = 198
CC2 = 80

body_recolour_CC1 = {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3, 140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}
body_recolour_CC2 = {136: CC2, 137: CC2+1, 138: CC2+2, 139: CC2+3, 140: CC2+4, 141: CC2+5, 142: CC2+6, 143: CC2+7}

# facts about 'standard' spritesheets, spritesheets varying from this will be painful
spriterow_height = 30
spritesheet_top_margin = 10
# wider than sprites, allows room for custom buy menu sprites, also to print cargo labels to aid drawing / debugging generated cargos
spritesheet_width = 425

# --- Cargo Maps ---- #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah

# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table

cement_silo_livery_recolour_maps = (("DFLT", {136: 53, 137: 54, 138: 6, 139: 57,
                                       140: 30, 141: 38, 142: 13, 143: 15}),)

silo_livery_recolour_maps = (("DFLT", {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3,
                                       140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}),)
"""
 # legacy silo remaps, cargo-specific
 ("DFLT", {136: 16, 137: 17, 138: 18, 139: 19,
           140: 20, 141: 21, 142: 22, 143: 23}),
 # BDMT and CMNT should be kept in sync
 ("BDMT", {136: 53, 137: 54, 138: 6, 139: 57,
           140: 30, 141: 38, 142: 13, 143: 15}),
 ("CBLK", {136: 1, 137: 2, 138: 3, 139: 4,
           140: 5, 141: 6, 142: 7, 143: 8}),
 ("CMNT", {136: 53, 137: 54, 138: 6, 139: 57,
           140: 30, 141: 38, 142: 13, 143: 15}),
 # food dropped, but use for flour / starch if added
 #("FOOD", {136: 16, 137: 18, 138: 8, 139: 10,
 #          140: 23, 141: 13, 142: 14, 143: 15}),
 ("KAOL", {136: 16, 137: 18, 138: 8, 139: 10,
           140: 23, 141: 13, 142: 14, 143: 15}),
 ("QLME", {136: 34, 137: 35, 138: 36, 139: 37,
           140: 38, 141: 39, 142: 14, 143: 15}),
 ("RUBR", {136: 40, 137: 41, 138: 42, 139: 43,
           140: 44, 141: 45, 142: 46, 143: 47}),
 ("SASH", {136: 145, 137: 146, 138: 147, 139: 150,
           140: 151, 141: 152, 142: 12, 143: 153}),
 ("SUGR", {136: 16, 137: 18, 138: 8, 139: 10,
           140: 23, 141: 13, 142: 14, 143: 15}),)
"""
box_livery_recolour_maps = (("DFLT", {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3,
                                      140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3,
                                      44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7,
                                      CC2: CC1, CC2+1: CC1+1, CC2+2: CC1+2, CC2+3: CC1+3,
                                      CC2+4: CC1+4, CC2+5: CC1+5, CC2+6: CC1+6, CC2+7: CC1+7}),)

caboose_livery_recolour_maps = (# DFLT can be used twice here with no problems, it's not a unique key
                                ("DFLT", {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3,
                                          140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7,
                                          40: CC2, 41: CC2+1, 42: CC2+2, 43: CC2+3,
                                          44: CC2+4, 45: CC2+5, 46: CC2+6, 47: CC2+7}),
                                ("DFLT", {136: CC2, 137: CC2+1, 138: CC2+2, 139: CC2+3,
                                          140: CC2+4, 141: CC2+5, 142: CC2+6, 143: CC2+7,
                                          40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3,
                                          44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),)

carbon_black_hopper_car_livery_recolour_maps = (# only one livery provided here, black
                                                ("DFLT", {136: 1, 137: 2, 138: 3, 139: 4,
                                                     140: 5, 141: 6, 142: 7, 143: 8,
                                                     154: 1, 155: 2, 156: 3, 157: 4,
                                                     158: 5, 159: 6, 160: 7, 161: 8}),)

chemicals_tank_car_livery_recolour_maps = (("DFLT", {136: 16, 137: 18, 138: 19, 139: 20,
                                                     140: 21, 141: 22, 142: 23, 143: 14}),)

covered_hopper_car_livery_recolour_maps = (("DFLT", {136: 72, 137: 73, 138: 74, 139: 75,
                                                     140: 76, 141: 77, 142: 78, 143: 79,
                                                     96: 16, 97: 17, 98: 18, 99: 19,
                                                     100: 20, 101: 21, 102: 22, 103: 23,
                                                     154: 72, 155: 73, 156: 74, 157: 75,
                                                     158: 76, 159: 77, 160: 78, 161: 79}),)

# the maps are lacking restraint, there are 3 different recolour ranges, allowing for solebar, body and tarp colours
"""
# !! covhop alt liveries ??
                                           ("DFLT", {136: 4, 137: 5, 138: 6, 139: 7,
                                                     140: 9, 141: 10, 142: 11, 143: 13,
                                                     96: CC1, 97: CC1+1, 98: CC1+2, 99: CC1+3,
                                                     100: CC1+4, 101: CC1+5, 102: CC1+6, 103: CC1+7,
                                                     154: 4, 155: 5, 156: 6, 157: 7,
                                                     158: 9, 159: 10, 160: 11, 161: 13}),

                                                ("CMNT", {136: 53, 137: 54, 138: 6, 139: 57,
                                                          140: 30, 141: 38, 142: 12, 143: 14,
                                                          96: CC1, 97: CC1+1, 98: CC1+2, 99: CC1+3,
                                                          100: CC1+4, 101: CC1+5, 102: CC1+6, 103: CC1+7,
                                                          154: 53, 155: 54, 156: 6, 157: 57,
                                                          158: 30, 159: 38, 160: 12, 161: 14}),
                                                ("KAOL", {136: 6, 137: 7, 138: 8, 139: 9,
                                                          140: 11, 141: 12, 142: 13, 143: 14,
                                                          96: 1, 97: 2, 98: 3, 99: 4,
                                                          100: 5, 101: 6, 102: 7, 103: 8,
                                                          154: CC1, 155: CC1+1, 156: CC1+2, 157: CC1+3,
                                                          158: CC1+4, 159: CC1+5, 160: CC1+6, 161: CC1+7}),
                                                ("QLME", {136: 34, 137: 35, 138: 36, 139: 37,
                                                          140: 38, 141: 39, 142: 14, 143: 15,
                                                          96: CC1, 97: CC1+1, 98: CC1+2, 99: CC1+3,
                                                          100: CC1+4, 101: CC1+5, 102: CC1+6, 103: CC1+7,
                                                          154: 34, 155: 35, 156: 36, 157: 37,
                                                          158: 38, 159: 39, 160: 14, 161: 15}),
                                                ("RUBR", {136: 40, 137: 41, 138: 42, 139: 43,
                                                          140: 44, 141: 45, 142: 46, 143: 47,
                                                          96: 1, 97: 2, 98: 3, 99: 4,
                                                          100: 5, 101: 6, 102: 7, 103: 8,
                                                          154: 40, 155: 41, 156: 42, 157: 43,
                                                          158: 44, 159: 45, 160: 46, 161: 47}),
                                                ("SALT", {136: 112, 137: 113, 138: 33, 139: 115,
                                                          140: 35, 141: 118, 142: 38, 143: 39,
                                                          96: CC1, 97: CC1+1, 98: CC1+2, 99: CC1+3,
                                                          100: CC1+4, 101: CC1+5, 102: CC1+6, 103: CC1+7,
                                                          154: 112, 155: 113, 156: 33, 157: 115,
                                                          158: 35, 159: 118, 160: 38, 161: 39})
"""

coil_car_livery_recolour_maps = (("DFLT", body_recolour_CC1),)

curtain_side_livery_recolour_maps = (("DFLT", body_recolour_CC1),)

edibles_tank_car_livery_recolour_maps = (("DFLT", {}),)

fruit_veg_livery_recolour_maps = (("DFLT", {136: CC2, 137: CC2+1, 138: CC2+2, 139: CC2+3,
                                            140: CC2+4, 141: CC2+5, 142: CC2+6, 143: CC2+7,
                                            40: 71, 41: 72, 42: 73, 43: 74,
                                            44: 75, 45: 77, 46: 78, 47: 79,
                                            CC1: 71, CC1+1: 72, CC1+2: 73, CC1+3: 74,
                                            CC1+4: 75, CC1+5: 77, CC1+6: 78, CC1+7: 79}),)

# minimalist for grain hoppers, just body colour (others were tried but found to be blah blah)
grain_hopper_car_livery_recolour_maps = (("DFLT", body_recolour_CC1),)

livestock_livery_recolour_maps = (("DFLT", body_recolour_CC2),)

minerals_covered_hopper_car_livery_recolour_maps = (("DFLT", {136: 6, 137: 7, 138: 8, 139: 9,
                                                              140: 11, 141: 12, 142: 13, 143: 14,
                                                              96: 1, 97: 2, 98: 3, 99: 4,
                                                              100: 5, 101: 6, 102: 7, 103: 8,
                                                              154: CC1, 155: CC1+1, 156: CC1+2, 157: CC1+3,
                                                              158: CC1+4, 159: CC1+5, 160: CC1+6, 161: CC1+7}),)

pellet_hopper_car_livery_recolour_maps = (("DFLT", {136: 16, 137: 17, 138: 18, 139: 19,
                                                    140: 20, 141: 21, 142: 22, 143: 23}),)

oil_tank_car_livery_recolour_maps = (("DFLT",  {136: 1, 137: 2, 138: 3, 139: 4,
                                                140: 5, 141: 6, 142: 7, 143: 8}),)

refrigerated_livery_recolour_maps = (("DFLT", {136: 18, 137: 19, 138: 20, 139: 21,
                                               140: 22, 141: 13, 142: 14, 143: 15,
                                               40: 18, 41: 19, 42: 20, 43: 21,
                                               44: 22, 45: 13, 46: 14, 47: 15,
                                               CC2: CC1, CC2+1: CC1+1, CC2+2: CC1+2, CC2+3: CC1+3,
                                               CC2+4: CC1+4, CC2+5: CC1+5, CC2+6: CC1+6, CC2+7: CC1+7}),)

sliding_wall_livery_recolour_maps = (("DFLT", {40: 4, 41: 5, 42: 6, 43: 7,
                                               44: 20, 45: 21, 46: 22, 47: 13}),)

tarpaulin_car_livery_recolour_maps = (("DFLT", body_recolour_CC2),)
