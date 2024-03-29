from roster import Roster

# list in buy menu order
engine_module_names = [
    # "challenger", # for NA roster
    # branch express
    "lark",
    "merrylegs",
    "decapod",
    "proper_job",
    "stag",
    "kelpie",
    "foxhound",
    "griffon",
    "lynx",
    "pinhorse",
    "argus",
    "booster",
    "tornado",
    # express
    "reliance",
    "spinner",
    "carrack",
    "braf",
    "tencendur",
    "diablo",
    "thunderer",
    "daring",
    "merlion",
    "shredder",
    "centaur",
    "swift",
    "strongbow",
    "arrow",
    "wyvern",
    "tenacious",
    "intrepid",
    "resilient",
    "rapid",
    "pegasus",
    "streamer",
    "hawkinge",
    "dragon",
    "vulcan",
    "falcon",
    "onslaught",
    "dreadnought",
    "defiant",
    "relentless",
    "dynamo",
    "cyclone",
    "shoebox",
    "ultra_shoebox",
    "hurly_burly",
    "moor_gallop",
    "roarer",
    "fury",
    "constance",
    "stalwart",
    "zebedee",
    "screamer",
    "revolution",
    "avenger",
    "sizzler",
    # branch freight
    "buffalo",
    "saxon",
    "yak",
    "little_bear",
    "captain_steel",
    "goliath",
    "general_endeavour",
    "stoat",
    "zest",
    # freight
    "hercules",
    "eastern",
    "celt",
    "haar",
    "trojan",
    "growler",
    "viking",
    "slug",
    "xerxes",
    "keen",
    "vigilant",
    "mainstay",
    "yillen",
    "maelstrom",
    "doineann",
    "doubletide",
    "girt_licker",
    "lemon",
    "esk",
    "chinook",
    "withershins",
    "lion",
    "grid",
    "bone",
    "toaster",
    "cheddar_valley",
    "stentor",
    "flindermouse",
    "dryth",
    "peasweep",
    "resistance",
    "tincans",
    "flanders_storm",
    "quietus",
    # gronks / snowploughs
    "grub",
    "lamia",
    "fireball",
    "gronk",
    "chuggypig",
    "progress",
    "magnum_90",
    "snowplough_pony_gen_2",
    # cargo sprinter
    "cargo_sprinter",
    # auto-coach (only one as autoreplace can't handle mixed cargo articulated consists)
    "auto_coach_pony_gen_2",
    # railbuses
    "clipper",
    "clipper_single",
    "skipper",
    "skipper_single",
    "zipper",
    "zipper_single",
    # diesel railcars
    "deasil",
    "slammer",
    "tin_rocket",
    "happy_train",
    "gowsty",
    "scooby",
    "plastic_postbox",
    # electric railcars
    "athena",
    "geronimo",
    "breeze",
    "zeus",
    "ares",
    "dover",
    "jupiter",
    "pylon",
    # express electric railcars
    "high_flyer",
    "sunshine_coast",
    "olympic",
    "chronos",
    "nimbus",
    # brit high speed pax
    "firebird",
    "blaze",
    "helm_wind_cab",
    "helm_wind_middle_passenger",
    "helm_wind_middle_mail",
    "alize_cab",
    "alize_middle_passenger",
    "alize_middle_mail",
    "brenner_cab",
    "brenner_middle_passenger",
    "brenner_middle_mail",
    "skeiron_cab",
    "skeiron_middle_passenger",
    "skeiron_middle_mail",
    # driving cab cars
    "driving_cab_passenger_pony_gen_4",
    "driving_cab_passenger_pony_gen_5",
    "driving_cab_high_speed_passenger_pony_gen_5",
    "driving_cab_high_speed_passenger_pony_gen_6",
    "driving_cab_mail_pony_gen_5",
    "driving_cab_high_speed_mail_pony_gen_5",
    "driving_cab_high_speed_mail_pony_gen_6",
    # metro
    "serpentine",
    "poplar",
    "westbourne",
    "hammersmith",
    "fleet",
    "canary",
    "longwater",
    "ravensbourne",
    "tyburn",
    "wandle",
    "tideway",
    "bankside",
    "debden",
    "cringle",
    "mulberry",
    "walbrook",
    "borax",
    "angerstein",
    # ng engines
    "cheese_bug",
    "bean_feast",
    "pikel",
    "boar_cat",
    "thor",
    "alfama",
    "gargouille",
    "solano",
    "lebeche",
    "tyrconnell",
    "nile",
    "hinterland",
    "rockhampton",
    "higuma",
    # ng railcars
    "mumble",
    "mumble_single",
    "snapper",
    "snapper_single",
    "zorro",
    "ruby",
    "golfinho",
    "stratos",
    "driving_cab_passenger_ng_pony_gen_4",
    "driving_cab_panoramic_passenger_ng_pony_gen_4",
]

# these can be alphabetised, the buy menu order is enforced in global constants
wagon_modules_provided_by_other_rosters = {}


def main():
    return Roster(
        id="pony",
        numeric_id=1,
        # note that the grf name is Iron Horse, as the pony roster was released for many years under that name, and changing it would needlessly confuse players
        # but to avoid overloading the word 'horse', which is widely used in src, we continue using 'pony' as the roster id
        grf_name="iron-horse",
        grfid=r"CA\12\22",
        str_grf_name="Iron Horse",
        # ELRL, ELNG is mapped to RAIL, NG etc
        # default intro dates per generation, can be over-ridden if needed by setting intro_year kw on consist
        intro_years={
            "RAIL": [1860, 1900, 1930, 1960, 1990, 2020],
            "METRO": [1900, 1950, 2000],
            "NG": [1860, 1910, 1960, 2010],
        },
        # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
        # speeds roughly same as RH trucks of same era + 5mph or so, and a bit higher at the top end (back and forth on this many times eh?),
        # NG is Corsican-style 1000mm, native brit NG is not a thing for gameplay
        speeds={
            "RAIL": {
                # gen 5 and 6 held down by design, really fast freight is imbalanced
                "standard": [
                    45,
                    45,
                    60,
                    75,
                    87,
                    87,
                ],
                # match standard, except gen 6
                "suburban": [45, 45, 60, 75, 87, 99],
                # smaller steps in gen 5 and 6, balances against faster HSTs
                "express": [
                    60,
                    75,
                    90,
                    105,
                    120,
                    120,
                ],
                "express_on_lgv": [
                    0,
                    0,
                    0,
                    0,
                    140,
                    140,
                ],
                "hst": [0, 0, 0, 112, 128, 128],
                "hst_on_lgv": [0, 0, 0, 0, 140, 140],
                "very_high_speed": [0, 0, 0, 0, 128, 128],
                "very_high_speed_on_lgv": [0, 0, 0, 0, 155, 186],
            },
            "METRO": {
                "standard": [45, 55, 65]
                # only standard for metro in Pony
            },
            "NG": {
                "standard": [
                    45,
                    45,
                    60,
                    60,
                ],
                # NG standard/suburban/express same in Pony, balanced against trams, RVs
                # suburban has to be provided as the mail railcar expects it, just copying it in is easiest solution
                "suburban": [45, 45, 60, 75],
                # NG express breaks from standard in gen 4
                "express": [45, 45, 60, 75],
            },
        },
        # capacity factor per generation, will be multiplied by vehicle length
        freight_car_capacity_per_unit_length={
            "RAIL": [4, 4, 5, 5.5, 6, 6],
            "NG": [3, 3, 4, 4],
            "METRO": [4, 5, 6],
        },
        pax_car_capacity_per_unit_length={
            "RAIL": [3, 3.75, 4.5, 5.25, 6, 6],
            "NG": [3, 5, 5, 6],
        },
        pax_car_capacity_types={
            "default": {
                "multiplier": 1,
                "loading_speed_multiplier": 1,
            },
            "high_capacity": {
                "multiplier": 1.5,
                "loading_speed_multiplier": 1.75,
            },
            "restaurant": {
                "multiplier": 0.45,
                "loading_speed_multiplier": 1,
            },
            # very specifically tuned multiplier against combine consists
            "autocoach_combine": {
                "multiplier": 2.7,
                "loading_speed_multiplier": 1.75,
            },
            # very specifically tuned multiplier against combine consists
            "railbus_combine": {
                "multiplier": 2.5,
                "loading_speed_multiplier": 1.75,
            },
            "railbus_combine_ng_1": {
                "multiplier": 2,
                "loading_speed_multiplier": 1.5,
            },
            "railbus_combine_ng_2": {
                "multiplier": 1.5,
                "loading_speed_multiplier": 1.25,
            },
        },
        # freight car weight factor varies slightly by gen, reflecting modern cars with lighter weight
        train_car_weight_factors=[0.5, 0.5, 0.5, 0.48, 0.44, 0.40],
        # specify lists of cc2 colours, and an option to remap all the cc1 to a specific other cc (allowing multiple input colours to map to one result)
        # generally, reuse of these is encouraged, they're (mostly) just metadata and can be repeated multiple times for different spriterows of a vehicle
        # keep alphabetised
        engine_and_pax_mail_car_liveries={
            "ARC": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_GREY", "COLOUR_GREY"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                ],
            },
            "BANGER_BLUE": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                ],
            },
            "DB_SCHENKER": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                ],
            },
            "DUTCH_1986": {
                "remap_to_cc": {
                    "company_colour1": "COLOUR_GREY",
                    "company_colour2": "company_colour1",
                },
                "forced_intro_year": 1986,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_YELLOW", "COLOUR_WHITE"),
                    ("COLOUR_GREY", "COLOUR_WHITE"),
                ],
            },
            "DUTCH": {
                "remap_to_cc": {
                    "company_colour1": "COLOUR_GREY",
                    "company_colour2": "company_colour1",
                },
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_YELLOW", "COLOUR_WHITE"),
                    ("COLOUR_GREY", "COLOUR_WHITE"),
                ],
            },
            "EWS": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_PINK", "COLOUR_YELLOW"),
                ],
            },
            "FREIGHT_BLACK": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                ],
            },
            "FREIGHTLINER_GBRF": {
                # note the remap to yellow, allowing 1cc wagons to be whatever player chooses
                "remap_to_cc": {
                    "company_colour1": "COLOUR_YELLOW",
                    "company_colour2": "company_colour1",
                },
                "docs_image_input_cc": [
                    ("COLOUR_PALE_GREEN", "COLOUR_YELLOW"),
                    ("COLOUR_DARK_GREEN", "COLOUR_YELLOW"),
                    ("COLOUR_GREEN", "COLOUR_YELLOW"),
                    ("COLOUR_MAUVE", "COLOUR_YELLOW"),
                ],
            },
            "INDUSTRIAL_BROWN": {
                "remap_to_cc": {
                    "company_colour1": "COLOUR_BROWN",
                    "company_colour2": "company_colour2",
                },
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                ],
            },
            "INDUSTRIAL_YELLOW": {
                "remap_to_cc": {
                    "company_colour1": "COLOUR_YELLOW",
                    "company_colour2": "company_colour2",
                },
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                ],
            },
            "INTERCITY_RASPBERRY_RIPPLE": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_PINK", "COLOUR_WHITE"),
                    ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
                ],
            },
            "LARGE_LOGO": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                ],
            },
            "LOADHAUL": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_ORANGE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_BLUE", "COLOUR_WHITE"),
                ],
            },
            "RAILFREIGHT_RED_STRIPE": {
                "remap_to_cc": {
                    "company_colour1": "COLOUR_GREY",
                    "company_colour2": "company_colour1",
                },
                "forced_intro_year": 1975,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_PINK", "COLOUR_WHITE"),
                ],
            },
            "RAILFREIGHT_TRIPLE_GREY": {
                # note the remap to white, to provide lightest of the triple greys as cc1
                "remap_to_cc": {
                    "company_colour1": "COLOUR_WHITE",
                    "company_colour2": "company_colour1",
                },
                "forced_intro_year": 1986,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_PINK", "COLOUR_WHITE"),
                ],
            },
            "RAILFREIGHT_TRIPLE_GREY_COAL": {
                # note the remap to white, to provide lightest of the triple greys as cc1
                "remap_to_cc": {
                    "company_colour1": "COLOUR_WHITE",
                    "company_colour2": "company_colour1",
                },
                "forced_intro_year": 1986,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                ],
            },
            "RES": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_BLUE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_LIGHT_BLUE"),
                ],
            },
            "ROYAL_MAIL": {
                "remap_to_cc": {
                    "company_colour1": "COLOUR_RED",
                    "company_colour2": "company_colour2",
                },
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_LIGHT_BLUE"),
                ],
            },
            "SWOOSH": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
                ],
            },
            "SWOOSH_1995": {
                "remap_to_cc": None,
                "forced_intro_year": 1995,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
                ],
            },
            "SWOOSH_2000": {
                "remap_to_cc": None,
                "forced_intro_year": 2000,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
                ],
            },
            "TGV_LA_POSTE": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_YELLOW", "COLOUR_BLUE"),
                ],
            },
            "TUBE": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_BLUE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_DARK_BLUE"),
                ],
            },
            # the default "nothing" livery
            "VANILLA": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_BLUE"),
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                ],
            },
            "WHITE_STRIPE": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
                ],
            },
            "WHITE_STRIPE_1995": {
                "remap_to_cc": None,
                "forced_intro_year": 1995,
                "docs_image_input_cc": [
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
                ],
            },
            "YEOMAN": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_GREY"),
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_GREY"),
                    ("COLOUR_ORANGE", "COLOUR_WHITE"),
                ],
            },
        },
        # lists of 2-tuple (livery_name, relative_spriterow_num) for pax / mail vehicles
        # buy menu order will match list order
        # - livery name comes from roster engine_and_pax_mail_car_liveries
        # - relative_spriterow_num allows reordering sprites relative to spritesheet
        pax_mail_livery_groups={
            "default_pax_liveries": [("VANILLA", 0), ("VANILLA", 1)],
            "gen_5_and_6_pax_liveries": [
                ("VANILLA", 0),
                ("VANILLA", 1),
                ("SWOOSH_2000", 2),
                ("SWOOSH_2000", 3),
            ],
            "suburban_pax_liveries": [
                ("VANILLA", 1),
                ("VANILLA", 0),
            ],
            "default_mail_liveries": [
                ("VANILLA", 3),
                ("VANILLA", 0),
                ("VANILLA", 1),
                ("VANILLA", 2),
                ("ROYAL_MAIL", 4),
            ],
            "gen_5_and_6_mail_liveries": [
                ("VANILLA", 5),
                ("VANILLA", 0),
                ("VANILLA", 1),
                ("SWOOSH_2000", 2),
                ("SWOOSH_2000", 3),
                ("VANILLA", 4),
                ("ROYAL_MAIL", 6),
            ],
            "diesel_railcar_mail_liveries": [
                ("RES", 2),
                ("INTERCITY_RASPBERRY_RIPPLE", 0),
                ("WHITE_STRIPE", 1),
                ("VANILLA", 3),
                ("ROYAL_MAIL", 4),
            ],
            "electric_railcar_mail_liveries": [
                ("VANILLA", 3),
                ("INTERCITY_RASPBERRY_RIPPLE", 0),
                ("WHITE_STRIPE", 1),
                ("RES", 2),
                ("ROYAL_MAIL", 4),
            ],
            "dvt_mail_liveries": [
                ("VANILLA", 0),
                ("VANILLA", 1),
                ("VANILLA", 2),
                ("VANILLA", 3),
            ],
            "metro_pax_liveries": [
                ("TUBE", 0),
                ("VANILLA", 1),
            ],
            "metro_mail_liveries": [
                ("TUBE", 0),
                ("VANILLA", 1),
                ("ROYAL_MAIL", 2),
            ],
        },
        engine_module_names=engine_module_names,
        wagon_modules_provided_by_other_rosters=wagon_modules_provided_by_other_rosters,
    )
