from roster import Roster

# list in buy menu order
engine_module_names = [
    # challenger, # for NA roster
    # branch express
    # foo,
    # express (electro-diesels with non-standard position in power/length tree)
    # foo,
    # express
    ## AC
    "ae_3_5",
    "sbb_fb_4_4",
    "saas_be_4_4",
    "obb_1040",
    "sbb_eem_923",
    "ae_3_6_1",
    "obb_1570",
    "obb_1170_2",
    "re_4_4_i",
    "obb_1163",
    "vectron_dual_mode",
    ## DC
    "hungarian_2d2_400",
    ## AC
    "ae_4_7",
    "obb_1041",
    "obb_1141",
    "re_450",
    "obb_1014",
    ## DC
    "fs_e330",
    "fs_e428",
    "fs_e444",
    "fs_e464",
    "fs_e464_upgrade",
    ## AC
    "drg_e_16",
    "obb_1010",
    "obb_1042",
    "obb_1142",
    "fs_e412",
    ## DC
    "fs_e636",
    "fs_e646",
    "fs_e656",
    "fs_e656_upgraded",
    ## AC
    "bls_ae_6_8",
    "bls_ae_4_4",
    "bls_re_4_4",
    "sob_re_446",
    ## DC
    "plm_2cc2_3400",
    "cc_7100",
    "bb_7200",
    "bb_22200",
    "bb_22200_upgraded",
    ## AC
    "obb_1044",
    "re_460",
    "re_465",
    ## DC
    "cc_6500",
    "bb_26000",
    "bb_26000_upgraded",
    # high powered railcars
    "high_power_railcar_2",
    "high_power_railcar_3",
    "high_power_railcar_4",
    "high_power_railcar_5",
    # driving cab cars
    # foo,
    # branch freight
    "de_6_6",
    # freight
    "trient",
    ## AC
    "krokodil_ce_6_8",
    "krokodil_be_6_8",
    "sbb_ee_6_6_ii",
    "mthb_re_486",
    ## DC
    "po_2d2_5500",
    "bb_25200",
    "bb_27000",
    ## AC
    "sbb_ae_4_6",
    "sbb_re_4_4_ii",
    "re_430",
    "re_430_lion",
    ## DC
    "fs_e633",
    "fs_e652",
    "traxx_e_494",
    ## AC
    "bls_ae_8_8",
    "bls_re_475",
    ## DC
    "bb_8100_duo",
    "bb_8500_duo",
    ## AC
    "re_6_6",
    "re_6_6_ii",
    ## DC
    # joker engines / snowploughs
    # "snowplough_ibex_gen_2",
    # cargo sprinter
    # foo,
    # auto-coach (only one as autoreplace can't handle mixed cargo articulated consists)
    # foo,
    # railbuses
    # foo,
    # diesel railcars
    # foo,
    # electric railcars
    ## AC
    "emu_ibex_2",
    "emu_ibex_3",
    "emu_ibex_4",
    "emu_ibex_5",
    "emu_ibex_6",
    ## DC
    # express electric railcars
    # foo,
    # high speed pax
    # AC
    "rapide_cab",
    "rapide_middle_mail",
    "rapide_middle_passenger",
    # metro
    # foo,
    # ng engines
    # foo,
    # ng railcars
    # foo,
]

# these can be alphabetised, the buy menu order is enforced in global constants
wagon_modules_provided_by_other_rosters = {
    "pony": [
        "acid_tank_cars",
        "carbon_black_hopper_cars",
        "cement_silo_cars",
        "coil_covered_cars_asymmetric",
        "cryo_tank_cars",
        "express_intermodal_cars",
        "flat_cars",
        "goods_box_cars",
        "heavy_duty_dump_cars",
        "heavy_duty_flat_cars",
        "ingot_cars",
        "intermodal_cars",
        "kaolin_hopper_cars",
        "log_cars",
        "ore_dump_cars",
        "pressure_tank_cars",
        "product_tank_cars",
        "reefer_cars_type_1",
        "reefer_cars_type_2",
        "silo_cars",
        "slag_ladle_cars",
        "sliding_roof_cars",
        "sliding_wall_cars",
        "sulphur_tank_cars",
        "tank_cars",
        "tarpaulin_cars",
        "torpedo_cars",
        "vehicle_parts_box_cars",
    ],
}


def main():
    return Roster(
        id="ibex",
        numeric_id=3,
        grf_name="iron-ibex",
        grfid=r"CA\12\21",
        str_grf_name="Iron Ibex",
        # ELRL, ELNG is mapped to RAIL, NG etc
        # default intro dates per generation, can be over-ridden if needed by setting intro_year kw on consist
        intro_years={
            "RAIL": [1885, 1912, 1939, 1966, 1993, 2020],
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
                "express": [
                    55,
                    75,
                    87,
                    100,
                    125,
                    140,
                ],
                "hst": [0, 0, 0, 112, 125, 125],
                "hst_on_lgv": [0, 0, 0, 112, 125, 140],
                "very_high_speed": [0, 0, 0, 0, 125, 125],
                "very_high_speed_on_lgv": [0, 0, 0, 0, 140, 186],
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
            "combine_consist_mail_pax": {
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
        engine_and_pax_mail_car_liveries={
            "SWOOSH": {
                # this is just a fallback for some special cases, such as snowploughs
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                ],
            },
            "FOO": {
                # optional remap, allowing 1cc wagons to be whatever player chooses
                # "remap_to_cc": {"company_colour1": "company_colour1", "company_colour2": "company_colour2"},
                "docs_image_input_cc": [
                    ("COLOUR_YELLOW", "COLOUR_PALE_GREEN"),
                    ("COLOUR_ORANGE", "COLOUR_DARK_GREEN"),
                    ("COLOUR_ORANGE", "COLOUR_GREEN"),
                    ("COLOUR_CREAM", "COLOUR_MAUVE"),
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
        # buy menu order will match list order
        # - livery name comes from roster engine_and_pax_mail_car_liveries
        # - relative_spriterow_num allows reordering sprites relative to spritesheet
        pax_mail_livery_groups={
            "default_pax_liveries": [("VANILLA", 0)],
            "suburban_pax_liveries": [
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
        wagon_modules_provided_by_other_rosters=wagon_modules_provided_by_other_rosters,
    )
