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

silo_livery_recolour_maps = (("DFLT", {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3,
                                       140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}),
                             ("CMNT", {136: 16, 137: 17, 138: 18, 139: 19,
                                       140: 20, 141: 21, 142: 22, 143: 23}))

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

coil_car_livery_recolour_maps = (("DFLT", {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3,
                                           140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}),)

cryo_tank_car_livery_recolour_maps = (("DFLT", {136: 5, 137: 7, 138: 9, 139: 11,
                                                140: 12, 141: 13, 142: 14, 143: 15}),
                                      ("CHLO", {136: 154, 137: 155, 138: 157, 139: 158,
                                                140: 159, 141: 159, 142: 160, 143: 161}),)

chemicals_tank_car_livery_recolour_maps = (("DFLT", {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3,
                                                     140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}),)

curtain_side_livery_recolour_maps = (("DFLT", {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3,
                                               140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}),)

edibles_tank_car_livery_recolour_maps = (("DFLT", {}),)

fruit_veg_livery_recolour_maps = (("DFLT", {136: CC2, 137: CC2+1, 138: CC2+2, 139: CC2+3,
                                            140: CC2+4, 141: CC2+5, 142: CC2+6, 143: CC2+7,
                                            40: 71, 41: 72, 42: 73, 43: 74,
                                            44: 75, 45: 77, 46: 78, 47: 79,
                                            CC1: 71, CC1+1: 72, CC1+2: 73, CC1+3: 74,
                                            CC1+4: 75, CC1+5: 77, CC1+6: 78, CC1+7: 79}),)

livestock_livery_recolour_maps = (("DFLT", body_recolour_CC2),)

refrigerated_livery_recolour_maps = (("DFLT", {136: 18, 137: 19, 138: 20, 139: 21,
                                               140: 22, 141: 13, 142: 14, 143: 15,
                                               40: 18, 41: 19, 42: 20, 43: 21,
                                               44: 22, 45: 13, 46: 14, 47: 15,
                                               CC2: CC1, CC2+1: CC1+1, CC2+2: CC1+2, CC2+3: CC1+3,
                                               CC2+4: CC1+4, CC2+5: CC1+5, CC2+6: CC1+6, CC2+7: CC1+7}),)

sliding_wall_livery_recolour_maps = (("DFLT", {40: 4, 41: 5, 42: 6, 43: 7,
                                               44: 20, 45: 21, 46: 22, 47: 13}),)

tarpaulin_car_livery_recolour_maps = (("DFLT", {136: CC2, 137: CC2+1, 138: CC2+2, 139: CC2+3,
                                                140: CC2+4, 141: CC2+5, 142: CC2+6, 143: CC2+7}),)


# Containers
# !! simple recolouring, not cargo specific.  May need work ??  Could be cargo-specific??
container_recolour_maps = ({170 + i: CC1 + i for i in range(8)},
                           {170 + i: CC2 + i for i in range(8)},
                           {170 + i: 8 + i for i in range(8)})
