from roster import Roster

# list in buy menu order
engine_module_names = [
    # challenger, # for NA roster
    # branch express
    "f40ph",
    # express (electro-diesels with non-standard position in power/length tree)
    # foo,
    # express
    "sdp40f",
    "u28cg",
    # driving cab cars
    # foo,
    # branch freight
    "niagra",
    # freight
    "sd45",
    "u36c",
    # joker engines / snowploughs
    "snowplough_moose_gen_2",
    # cargo sprinter
    # foo,
    # auto-coach (only one as autoreplace can't handle mixed cargo articulated vehicles)
    # foo,
    # railbuses
    # foo,
    # diesel railcars
    # foo,
    # electric railcars
    # foo,
    # express electric railcars
    # foo,
    # high speed pax
    # foo,
    # metro
    # foo,
    # ng engines
    # foo,
    # ng railcars
    # foo,
]

# these can be alphabetised, the buy menu order is enforced in global constants
# these can delegate to another module for reuse of wagons; this is not a common case, but used for things like torpedo cars
# explicit wagon module lists per roster are better;
# implicit modules lists were tried (just using global_constants list and allowing failing imports), but was no less maintenance, and was faff
wagon_module_names_with_roster_ids = {}


def main():
    return Roster(
        id="moose",
        numeric_id=2,
        grf_name="iron-moose",
        grfid=r"CA\12\20",
        str_grf_name="Iron Moose",
        # ELRL, ELNG is mapped to RAIL, NG etc
        # default intro dates per generation, can be over-ridden if needed by setting intro_year kw on model def
        # Moose RAIL runs 10 years later than Horse, and is pinned to IRL UP Big Boy (1940) and UP Centennial (1970)
        intro_years={
            "RAIL": [1860, 1910, 1940, 1970, 2000, 2030],
            "METRO": [1900, 1950, 2000],
            "NG": [1860, 1905, 1950, 2000],
        },
        # default speeds per generation, can be over-ridden if needed by setting speed kw arg on model def
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
                # smaller steps in gen 5 and 6, balances against faster High Speed Rail
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
            "RAIL": [4, 4, 5, 5.5, 6, 6.5],
            "NG": [3, 3, 4, 4],
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
            # very specifically tuned multiplier against a single pony vehicle
            "autocoach_combine": {
                "multiplier": 2.7,
                "loading_speed_multiplier": 1.75,
            },
            "restaurant": {
                "multiplier": 0.45,
                "loading_speed_multiplier": 1,
            },
        },
        # freight car weight factor varies slightly by gen, reflecting modern cars with lighter weight
        train_car_weight_factors=[0.5, 0.5, 0.5, 0.48, 0.44, 0.40],
        # specify lists of cc2 colours, and an option to remap all the cc1 to a specific other cc (allowing multiple input colours to map to one result)
        engine_and_misc_car_liveries={
            # the default "nothing" livery
            "VANILLA": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_BLUE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_PALE_GREEN", "COLOUR_ORANGE"),
                ],
            },
        },
        # lists of 2-tuple (livery_name, relative_spriterow_num) for pax / mail vehicles
        # buy menu order will match list order
        # - livery name comes from roster engine_and_misc_car_liveries
        # - relative_spriterow_num allows reordering sprites relative to spritesheet
        pax_mail_livery_groups={
            "default_pax_liveries": [("VANILLA", 0)],
            "default_suburban_pax_liveries": [
                ("VANILLA", 0),
            ],
            "default_mail_liveries": [
                ("VANILLA", 0),
            ],
            "diesel_railcar_mail_liveries": [
                ("VANILLA", 0),
            ],
            "electric_railcar_mail_liveries": [
                ("VANILLA", 0),
            ],
            "default_metro_liveries": [
                ("VANILLA", 0),
            ],
        },
        engine_module_names=engine_module_names,
        wagon_module_names_with_roster_ids=wagon_module_names_with_roster_ids,
    )
