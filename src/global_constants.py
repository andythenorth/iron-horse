buy_menu_sort_order = ['sunk_rock_ferry',
                       'barletta_paddle_steamer',
                       'castle_point_steamer',
                       'fastnet_paddle_steamer',
                       'patos_island_vehicle_ferry',
                       'feodosiya_hydrofoil',
                       'matsushima_hydrofoil',
                       'capo_sandalo_vehicle_ferry',
                       'enoshima_catamaran_ferry',
                       'mount_blaze_catamaran_ferry',
                       'harbour_point_utility_vessel',
                       'endeavour_utility_catamaran',
                       'fish_island_trawler',
                       'cape_spear_trawler',
                       'thunder_bay_hovercraft',
                       'whitgift_freight_barge',
                       'little_cumbrae_freighter',
                       'saint_marie_barge_tug',
                       'lindau_freight_barge',
                       'altamira_freighter',
                       'marstein_freighter',
                       'frisco_bay_freighter',
                       'santorini_freighter',
                       'maspalomas_freighter',
                       'pine_island_log_tug',
                       'eddystone_tanker',
                       'hopetown_tanker',
                       'yokohama_tanker',
                       'shark_island_livestock_ship',
                       'nieuwpoort_container_feeder']

# shared lists of allowed classes, shared across multiple ship types
base_refits_by_class = {'empty': [],
                       'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                       'pax_mail': ['CC_PASSENGERS','CC_MAIL'],
                       'liquids': ['CC_LIQUID'],
                       'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                       'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

# used to construct the cargo table automatically
# stolen from BANDIT code which also offered option to specify random cargo variations - that part is not currently used in FISH
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
from ordered_dict_backport import OrderedDict
cargo_graphics_mappings = OrderedDict([('PASS', []), # pax first
                                       ('TOUR', []),
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
