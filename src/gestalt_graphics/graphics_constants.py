# colour defaults
CC1 = 198
CC2 = 80

body_recolour_CC1 = {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3, 140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}
body_recolour_CC2 = {136: CC2, 137: CC2+1, 138: CC2+2, 139: CC2+3, 140: CC2+4, 141: CC2+5, 142: CC2+6, 143: CC2+7}

# facts about 'standard' spritesheets, spritesheets varying from this will be painful
spriterow_height = 30
spritesheet_top_margin = 10
# assumes auto-buy menu sprite (from 7th column), not explicit buy menu
# wider than sprites, allows room to print cargo labels to aid drawing / debugging generated cargos
spritesheet_width = 400

# --- Cargo Maps ---- move to  #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah

# DYES
# PLAS
silo_livery_recolour_maps = (("OIL_", {136: 1, 137: 2, 138: 3, 139: 4,
                                         140: 5, 141: 6, 142: 7, 143: 8}),  # see note on oil above
                               # see note on DFLT above
                               ("DFLT", {136: 198, 137: 199, 138: 200, 139: 201,
                                         140: 202, 141: 203, 142: 204, 143: 205}),
                               ("SULP", {136: 62, 137: 63, 138: 64, 139: 65,
                                         140: 66, 141: 67, 142: 68, 143: 69}),
                               ("CHLO", {136: 154, 137: 155, 138: 156, 139: 157,
                                         140: 158, 141: 159, 142: 160, 143: 161}),
                               # RFPR deliberately 2CC to allow combining with 1CC livery details
                               ("RFPR", {136: 80, 137: 81, 138: 82, 139: 83,
                                         140: 84, 141: 85, 142: 86, 143: 87}),
                               ("RUBR", {136: 40, 137: 41, 138: 42, 139: 43,
                                         140: 44, 141: 45, 142: 46, 143: 47}),
                               ("PETR", {136: 16, 137: 17, 138: 18, 139: 19,
                                         140: 20, 141: 21, 142: 22, 143: 23}))

box_livery_recolour_maps = (# see note on DFLT above
                           ("DFLT", {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3,
                                     140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7,
                                     40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3,
                                     44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7,
                                     CC2: CC1, CC2+1: CC1+1, CC2+2: CC1+2, CC2+3: CC1+3,
                                     CC2+4: CC1+4, CC2+5: CC1+5, CC2+6: CC1+6, CC2+7: CC1+7}),)

caboose_livery_recolour_maps = (# see note on DFLT above
                               ("DFLT", body_recolour_CC1),)

fruit_veg_livery_recolour_maps = (# see note on DFLT above
                                 ("DFLT", body_recolour_CC1),)

refrigerated_livery_recolour_maps = (# see note on DFLT above
                                    ("DFLT", {136: 18, 137: 19, 138: 20, 139: 21,
                                              140: 22, 141: 13, 142: 14, 143: 15,
                                              40: 18, 41: 19, 42: 20, 43: 21,
                                              44: 22, 45: 13, 46: 14, 47: 15,
                                              CC2: CC1, CC2+1: CC1+1, CC2+2: CC1+2, CC2+3: CC1+3,
                                              CC2+4: CC1+4, CC2+5: CC1+5, CC2+6: CC1+6, CC2+7: CC1+7}),)

livestock_livery_recolour_maps = (# see note on DFLT above
                                 ("DFLT", body_recolour_CC2),)

# Containers
# !! simple recolouring, not cargo specific.  May need work ??  Could be cargo-specific??
container_recolour_maps = ({170 + i: CC1 + i for i in range(8)},
                           {170 + i: CC2 + i for i in range(8)},
                           {170 + i: 8 + i for i in range(8)})
