# colour defaults
CC1 = 198
CC2 = 80

# a convenience constant that holds a mapping for swapping CC1 and CC2 around
CC1_CC2_SWAP_MAP = {}
for i in range(8):
    CC1_CC2_SWAP_MAP[CC1 + i] = CC2 + i
    CC1_CC2_SWAP_MAP[CC2 + i] = CC1 + i

# facts about 'standard' spritesheets, spritesheets varying from this will be painful
spriterow_height = 30
spritesheet_top_margin = 10
spritesheet_width = 455

vehicles_input_dir = 'vehicles'

# --- Cargo Maps ---- #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah

# Livery Only
# broadly, keep cargos in alphabetical order for ease of reading
# OIL_ is in first position as the buy menu sprites should be the Oil sprites, and this is the easiest way to do it
# in principle that's wrong, because in a map without oil, the buy menu won't match the sprites of the vehicle when built
# try it and see what happens eh?
# DFLT label is a hack to provide specific livery for unknown cargos and should not be added to cargo translation table
tanker_livery_recolour_maps = (("OIL_", {136: 1, 137: 2, 138: 3, 139: 4, 140: 5, 141: 6, 142: 7, 143: 8}), # see note on oil above
                               ("DFLT", {136: 80, 137: 81, 138: 82, 139: 83, 140: 84, 141: 85, 142: 86, 143: 87}), # see note on DFLT above
                               ("SULP", {136: 62, 137: 63, 138: 64, 139: 65, 140: 66, 141: 67, 142: 68, 143: 69}),
                               ("RFPR", {136: 198, 137: 199, 138: 200, 139: 201, 140: 202, 141: 203, 142: 204, 143: 205}),
                               ("RUBR", {136: 40, 137: 41, 138: 42, 139: 43, 140: 44, 141: 45, 142: 46, 143: 47}),
                               ("PETR", {136: 16, 137: 17, 138: 18, 139: 19, 140: 20, 141: 21, 142: 22, 143: 23}))
                            #DYES
                            #PLAS

# Containers
# !! simple recolouring, not cargo specific.  May need work ??  Could be cargo-specific??
container_recolour_maps = ({170 + i: CC1 + i for i in range(8)},
                           {170 + i: CC2 + i for i in range(8)},
                           {170 + i: 8 + i for i in range(8)})

# Bulk
# keep cargos in alphabetical order for ease of reading
# SCMT *is* bulk cargo in this set, realism is not relevant here, went back and forth on this a few times :P
# first set of colours is cargo recolour, second is body recolour
bulk_cargo_recolour_maps = (("AORE", {170: 42, 171: 123, 172: 74, 173: 125, 174: 162, 175: 126, 176: 78,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("CASS", {170: 53, 171: 54, 172: 55, 173: 56, 174: 57, 175: 58, 176: 59,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("CLAY", {170: 55, 171: 56, 172: 57, 173: 77, 174: 78, 175: 79, 176: 80,
                                      40: 145, 41: 146, 42: 147, 43: 148, 44: 149, 45: 150, 46: 151, 47: 152}),
                            ("COAL", {170: 1, 171: 1, 172: 2, 173: 2, 174: 3, 175: 4, 176: 5,
                                      40: 16, 41: 17, 42: 18, 43: 19, 44: 20, 45: 21, 46: 22, 47: 23}),
                            ("CORE", {170: 1, 171: 32, 172: 25, 173: 27, 174: 34, 175: 56, 176: 59,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("GRVL", {170: 6, 171: 4, 172: 7, 173: 8, 174: 21, 175: 11, 176: 12,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("IORE", {170: 75, 171: 76, 172: 123, 173: 122, 174: 124, 175: 74, 176: 104,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("LIME", {170: 6, 171: 4, 172: 7, 173: 8, 174: 21, 175: 11, 176: 12,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("MNO2", {170: 1, 171: 16, 172: 3, 173: 17, 174: 18, 175: 19, 176: 20,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("NITR", {170: 37, 171: 38, 172: 38, 173: 39, 174: 39, 175: 69, 176: 69,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("PHOS", {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("PORE", {170: 40, 171: 72, 172: 73, 173: 33, 174: 33, 175: 63, 176: 63,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("POTA", {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}),
                            ("SAND", {170: 108, 171: 64, 172: 65, 173: 197, 174: 36, 175: 196, 176: 197,
                                      40: 7, 41: 8, 42: 9, 43: 10, 44: 11, 45: 12, 46: 13, 47: 14}),
                            ("SCMT", {170: 104, 171: 3, 172: 2, 173: 70, 174: 71, 175: 72, 176: 3,
                                      40: 1, 41: 2, 42: 3, 43: 4, 44: 5, 45: 6, 46: 7, 47: 8}),
                            ("SGBT", {170: 60, 171: 53, 172: 54, 173: 55, 174: 56, 175: 57, 176: 58,
                                      40: CC1, 41: CC1+1, 42: CC1+2, 43: CC1+3, 44: CC1+4, 45: CC1+5, 46: CC1+6, 47: CC1+7}))

# Piece
# 2-tuples, containing 2 lists (['LBL1', 'LBL2'], ['filename_1', 'filename_2'])
# this groups labels and sprites, but there's no obvious problem with that right now
# if a label can't share a group of sprites, it can repeat some filenames, that's just inefficient, but works
# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
piece_cargo_maps = ((['DFLT'], ['tarps_2cc_1']), # see note on DFLT above
                    (['BEER', 'DYES', 'EOIL', 'MILK', 'OIL_', 'PETR', 'RFPR', 'WATR'], ['barrels_silver']),
                    (['BDMT',], ['tarps_red_1']),
                    (['COPR'], ['copper_coils']),
                    (['ENSP',], ['tarps_gold_1']),
                    (['FMSP'], ['tarps_blue_1']),
                    (['FRUT'], ['fruit']),
                    (['JAVA'], ['coffee']),
                    (['GOOD'], ['crates_1']),
                    (['NUTS'], ['nuts']),
                    (['PAPR'], ['paper_coils']),
                    (['STEL'], ['steel_coils']),
                    (['WDPR'], ['lumber_planks']),
                    (['WOOD'], ['logs']))

# --- End Cargo Maps --- #
