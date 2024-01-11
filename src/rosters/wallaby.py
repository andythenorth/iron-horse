from roster import Roster

from vehicles import dl
from vehicles import mka
from vehicles import nile
from vehicles import rockhampton
from vehicles import silverfern_2
from vehicles import tyrconnell

def main():
    return Roster(
        id="wallaby",
        numeric_id=5,
        # note that the grf name is Iron Horse, as the pony roster was released for many years under that name, and changing it would needlessly confuse players
        # but to avoid overloading the word 'horse', which is widely used in src, we continue using 'pony' as the roster id
        grf_name="iron-wallaby",
        grfid=r"CA\12\23", # when bumping grfid, increment last digit(s) to whatever is last used across all iron-[x] grfs
        str_grf_name="Iron Wallaby",
        # ELRL, ELNG is mapped to RAIL, NG etc
        # default intro dates per generation, can be over-ridden if needed by setting intro_year kw on consist
        intro_years={
            "RAIL": [1860, 1900, 1930, 1960, 1990, 2020],
            "METRO": [1900, 1950, 2000],
            "NG": [1860, 1905, 1950, 2000],
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
                "hst": [0, 0, 0, 112, 128, 128],  # CABBAGE
                "hst_on_lgv": [0, 0, 0, 0, 140, 140],  # CABBAGE
                "very_high_speed": [0, 0, 0, 0, 128, 128],  # CABBAGE
                "very_high_speed_on_lgv": [0, 0, 0, 0, 155, 186],  # CABBAGE
            },
            "METRO": {
                "standard": [45, 55, 65]
                # only standard for metro in Pony
            },
            "NG": {
                "standard": [
                    45,
                    45,
                    55,
                    65,
                ],
                # NG standard/suburban/express same in Pony, balanced against trams, RVs
                # suburban has to be provided as the mail railcar expects it, just copying it in is easiest solution
                "suburban": [45, 45, 55, 65],
                # suburban has to be provided as the coaches/mail vans etc expect it, just copying it in is easiest solution
                "express": [45, 45, 55, 65],
            },
        },
        # capacity factor per generation, will be multiplied by vehicle length
        freight_car_capacity_per_unit_length={
            "RAIL": [4, 4, 5, 5.5, 6, 6],
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
            "restaurant": {
                "multiplier": 0.45,
                "loading_speed_multiplier": 1,
            },
            # very specifically tuned multiplier against combin consists
            "autocoach_combine": {
                "multiplier": 2.7,
                "loading_speed_multiplier": 1.75,
            },
            # very specifically tuned multiplier against combin consists
            "railbus_combine": {
                "multiplier": 2.5,
                "loading_speed_multiplier": 1.75,
            },
        },
        # freight car weight factor varies slightly by gen, reflecting modern cars with lighter weight
        train_car_weight_factors=[0.5, 0.5, 0.5, 0.48, 0.44, 0.40],
        # specify lists of cc2 colours, and an option to remap all the cc1 to a specific other cc (allowing multiple input colours to map to one result)
        # generally, reuse of these is encouraged, they're (mostly) just metadata and can be repeated multiple times for different spriterows of a vehicle
        # keep alphabetised
        engine_and_pax_mail_car_liveries={
            "FREIGHT_BLACK": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
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
            "SWOOSH": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
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
        },
        # lists of 2-tuple (livery_name, relative_spriterow_num) for pax / mail vehicles
        # buy menu order will match liast order
        # - livery name comes from roster engine_and_pax_mail_car_liveries
        # - relative_spriterow_num allows reordering sprites relative to spritesheet
        pax_mail_livery_groups={
            "default_pax_liveries": [
                ("VANILLA", 0),
                ("VANILLA", 1)
            ],
            "default_mail_liveries": [
                ("VANILLA", 3),
                ("VANILLA", 0),
                ("VANILLA", 1),
                ("VANILLA", 2),
            ],
        },
        # this list is manually maintained deliberately, even though it could be mostly automated using tech tree
        engines=[
            # branch express
            # N/A
            # express
            # N/A
            # branch freight
            # N/A
            # freight
            # N/A
            # gronks / snowploughs
            # N/A
            # cargo sprinter
            # N/A
            # auto-coach (only one as autoreplace can't handle mixed cargo articulated consists)
            # N/A
            # railbuses
            # N/A
            # diesel railcars
            # N/A
            # electric railcars
            # N/A
            # express electric railcars
            # N/A
            # high speed pax
            # N/A
            # driving cab cars
            # N/A
            # metro
            # N/A
            # ng engines
            mka,
            tyrconnell,
            nile,
            silverfern_2,
            rockhampton,
            dl,
            # ng railcars
            # N/A
        ],
    )
