# wagon ids are generic and are composed to specific vehicle ids elsewhere
# order is significant
buy_menu_sort_order_wagons = ['passenger_car',
                              'mail_car',
                              'combine_car',
                              'open_car',
                              'box_car',
                              'hopper_car',
                              'tank_car',
                              'flat_car',
                              'livestock_car',
                              'covered_hopper_car',
                              'edibles_tank_car',
                              'reefer_car',
                              'supplies_car',
                              'intermodal_flat_car',
                              'caboose_car',
                              'passenger_car_ng',
                              'mail_car_ng',
                              'open_car_ng',
                              'box_car_ng',
                              'tank_car_ng',
                              'flat_car_ng',
                              'livestock_car_ng']

# set (roster) <-> numeric id mapping
# vehicle IDs are in format nxxx where n is set numeric id
# first 1k IDs reserved, IDs must be < 16383, with 1000 IDs allocated per set
vehicle_set_id_mapping = {'brit': 1}

# sets have up to 500 IDs for main set, zero-based, and 400 IDs for 'extras' (metro, narrow gauge etc)
# 900-990 IDs are reserved in case we run into any 'wtf' stuff that needs a gap
# wagon IDs run 250-490 and 750-890, the 0-240 and 500-740 IDs in a vehicle set are reserved for engines
wagon_type_numeric_ids = {'caboose_car': 250, 'box_car': 260, 'covered_hopper_car': 270, 'flat_car': 280,
                          'hopper_car': 290, 'tank_car': 300, 'livestock_car': 310, 'mail_car': 320,
                          'reefer_car': 330, 'open_car': 340, 'passenger_car': 350, 'combine_car': 360,
                          'intermodal_flat_car': 370, 'edibles_tank_car': 380, 'supplies_car': 390,
                          'metro_car': 400, # metro car should be in #760+ range, but isn't; no need to break savegames by moving it
                          # extra (NG, maglev) wagon IDs start at 750, max extra wagon type ID is 890
                          # 750 is empty
                          'mail_car_ng': 750, 'box_car_ng': 760,  'flat_car_ng': 780,
                          'tank_car_ng' : 800, 'livestock_car_ng': 810,
                          'open_car_ng': 840, 'passenger_car_ng': 850}

# shared lists of allowed classes, shared across multiple vehicle types
# these lists are similar but not identical across Iron Horse, Squid, Road Hog etc
base_refits_by_class = {'empty': [],
                        'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                        'pax': ['CC_PASSENGERS'],
                        'mail': ['CC_MAIL'],
                        'liquids': ['CC_LIQUID'],
                        'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                        'flatcar_freight': ['CC_PIECE_GOODS'],
                        'hopper_freight': ['CC_BULK'],
                        'covered_hopper_freight': [],
                        'refrigerated_freight': ['CC_REFRIGERATED'],
                        'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

# rather than using disallowed classes (can cause breakage), specific labels are disallowed
# this is done per vehicle type, or added to global_constants for ease of reuse and updating
# these lists are similar but not identical across Iron Horse, Squid, Road Hog etc
disallowed_refits_by_label = {'non_hopper_freight': ['WOOD', 'SGCN', 'FICR', 'BDMT', 'WDPR', 'GRAI', 'WHEA', 'MAIZ', 'FRUT'],
                              'edible_liquids': ['MILK', 'WATR', 'BEER', 'FOOD'],
                              'non_edible_liquids': ['RFPR', 'OIL_', 'FMSP', 'PETR', 'RUBR'],
                              'non_flatcar_freight': ['FOOD', 'FISH', 'LVST', 'FRUT', 'BEER', 'MILK', 'JAVA', 'SUGR'],
                              'non_freight_special_cases': ['TOUR']}

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
gen_1_wagon_speeds = [65, 85]
gen_2_wagon_speeds = [85, 100]
gen_3_wagon_speeds = [100, None]
ng_wagon_speeds = [55, 55]

# capacity multipliers for capacity parameter
capacity_multipliers = [0.67, 1, 1.33]

param_adjust_vehicle_capacity = 1

# used to construct the cargo table automatically
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
cargo_labels = ['PASS', # pax first
                'TOUR',
                # "the mail must get through"
                'MAIL',
                # all other cargos - append new ones to end, don't change order
                'COAL',
                'IORE',
                'GRVL',
                'SAND',
                'AORE',
                'CORE',
                'CLAY',
                'SCMT',
                'WOOD',
                'LIME',
                'GOOD',
                'FOOD',
                'STEL',
                'FMSP',
                'ENSP',
                'BEER',
                'BDMT',
                'MNSP',
                'PAPR',
                'WDPR',
                'VEHI',
                'COPR',
                'DYES',
                'OIL_',
                'RFPR',
                'PETR',
                'PLAS',
                'WATR',
                'FISH',
                'CERE',
                'FICR',
                'FRVG',
                'FRUT',
                'GRAI',
                'LVST',
                'MAIZ',
                'MILK',
                'RUBR',
                'SGBT',
                'SGCN',
                'WHEA',
                'WOOL',
                'OLSD',
                'SUGR',
                'JAVA',
                #
                'NULL']

# meaning of grfid should be obvious :)
# (DanMacK is from canada, and IH starts in 1830)
grfid = r"CA\12\1E"

# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = 'chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = 'generated'

# this is for nml or grfcodec, don't need to use python path module here
graphics_path = 'generated/graphics/'

# cargo aging constant - OTTD default is 185
CARGO_AGE_PERIOD = 185

# OpenTTD's max date
max_game_date = 5000001

# id and numeric id for 1/8 long null trailing slice used to compose units to correct length
null_trailing_slice_id = 'null_trailing_slice'
null_trailing_slice_numeric_id = 1

# standard offsets for trains (n.b. length < 3 isn't possible with 3-part articulated vehicles)
default_train_offsets = {'3': [[-3, -23], [-3, -20], [6, -11], [5, -14], [-3, -12], [-14, -14], [-20, -11], [-8, -21]],
                         '4': [[-3, -21], [-4, -19], [2, -11], [3, -14], [-3, -12], [-14, -14], [-20, -11], [-8, -20]],
                         '5': [[-3, -20], [-6, -18], [0, -11], [1, -13], [-3, -12], [-16, -13], [-20, -11], [-8, -18]],
                         '6': [[-3, -20], [-8, -17], [-4, -11], [-1, -13], [-3, -12], [-16, -13], [-20, -11], [-8, -18]],
                         '7': [[-3, -18], [-8, -17], [-5, -11], [-1, -12], [-3, -12], [-17, -12], [-24, -11], [-10, -18]],
                         '8': [[-3, -17], [-10, -16], [-8, -11], [-4, -13], [-3, -10], [-17, -12], [-24, -11], [-10, -17]],
                         '9': [[-3, -19], [-10, -18], [-8, -12], [-4, -14], [-3, -10], [-19, -13], [-28, -12], [-12, -19]],
                         '10': [[-3, -19], [-12, -17], [-12, -12], [-6, -14], [-3, -12], [-19, -13], [-28, -12], [-12, -18]]}

# fix for depot view when sprites are on leadslice
xoffs_adjusts = {'3': 4, '4': 4, '5': 4, '6': 4, '7': 8, '8': 8, '9': 12, '10': 12}

# mapping from length of visible 'part' to internal slice lengths
slice_lengths = {3: (1,1,1),
                 4: (1,2,1),
                 5: (1,3,1),
                 6: (1,4,1),
                 7: (2,3,2),
                 8: (2,4,2),
                 9: (3,3,3),
                10: (3,4,3),
                11: (3,5,3),
                12: (4,4,4),
                13: (4,5,4),
                14: (4,6,4),
                15: (4,7,4),
                16: (4,8,4)}
