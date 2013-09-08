buy_menu_sort_order = ['growler',
                       'geep',
                       'passenger_car',
                       'mail_car',
                       'box_car_gen_1']

# shared lists of allowed classes, shared across multiple ship types
base_refits_by_class = {'empty': [],
                       'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                       'pax': ['CC_PASSENGERS'],
                       'mail': ['CC_MAIL'],
                       'liquids': ['CC_LIQUID'],
                       'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                       'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

# speed for each generation of wagons in mph
wagon_speeds = {'gen_1':75}

# used to construct the cargo table automatically
# stolen from BANDIT code which also offered option to specify random cargo variations - that part is not currently used in FISH
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
from ordered_dict_backport import OrderedDict
cargo_graphics_mappings = OrderedDict([('PASS', []), # pax first
                                       ('TOUR', []),
                                       # "the mail must get through"
                                       ('MAIL', []),
                                       # bulk-ish cargos
                                       ('COAL', []),
                                       ('IORE', []),
                                       ('GRVL', []),
                                       ('SAND', []),
                                       ('AORE', []),
                                       ('CORE', []),
                                       ('CLAY', []),
                                       ('SCMT', []),
                                       ('WOOD', []),
                                       ('LIME', []),
                                       # common express-ish / processed cargos
                                       ('GOOD', []),
                                       ('FOOD', []),
                                       ('STEL', []),
                                       ('FMSP', []),
                                       ('ENSP', []),
                                       ('BEER', []),
                                       ('BDMT', []),
                                       ('MNSP', []),
                                       ('PAPR', []),
                                       ('WDPR', []),
                                       ('VEHI', []),
                                       ('COPR', []),
                                       ('DYES', []),
                                       # liquid-ish cargos
                                       ('OIL_', []),
                                       ('RFPR', []),
                                       ('PETR', []),
                                       ('PLAS', []),
                                       ('WATR', []),
                                       # fish and farm cargos
                                       ('FISH', []),
                                       ('CERE', []),
                                       ('FICR', []),
                                       ('FRVG', []),
                                       ('FRUT', []),
                                       ('GRAI', []),
                                       ('LVST', []),
                                       ('MAIZ', []),
                                       ('MILK', []),
                                       ('RUBR', []),
                                       ('SGBT', []),
                                       ('SGCN', []),
                                       ('WHEA', []),
                                       ('WOOL', [])])

# this is for nml, don't need to use python path module here
graphics_path = 'src/graphics/'

# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = 'chameleon_cache'

# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

# OpenTTD's max date
max_game_date = 5000001
