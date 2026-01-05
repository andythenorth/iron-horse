from roster import Roster

# list in buy menu order
engine_module_names = [
    # challenger, # for NA roster
    # branch express
    # foo,
    # express (electro-diesels with non-standard position in power/length tree)
    # foo,
    # express
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
    "hungarian_2d2_400",
    "ae_4_7",
    "obb_1041",
    "obb_1141",
    "re_450",
    "obb_1014",
    "fs_e330",
    "fs_e428",
    "fs_e444",
    "fs_e464",
    "fs_e464_upgrade",
    "drg_e_16",
    "obb_1010",
    "obb_1042",
    "obb_1142",
    "fs_e412",
    "fs_e636",
    "fs_e646",
    "fs_e656",
    "fs_e656_upgraded",
    "bls_ae_6_8",
    "bls_ae_4_4",
    "bls_re_4_4",
    "sob_re_446",
    "plm_2cc2_3400",
    "cc_7100",
    "bb_7200",
    "bb_22200",
    "bb_22200_upgraded",
    "obb_1044",
    "re_460",
    "re_465",
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
    "krokodil_ce_6_8",
    "krokodil_be_6_8",
    "sbb_ee_6_6_ii",
    "mthb_re_486",
    "po_2d2_5500",
    "bb_25200",
    "bb_27000",
    "sbb_ae_4_6",
    "sbb_re_4_4_ii",
    "re_430",
    "re_430_lion",
    "fs_e633",
    "fs_e652",
    "traxx_e_494",
    "bls_ae_8_8",
    "bls_re_475",
    "bb_8100_duo",
    "bb_8500_duo",
    "re_6_6",
    "re_6_6_ii",
    # joker engines / snowploughs
    # "snowplough_ibex_gen_2",
    # cargo sprinter
    # foo,
    # autocoach (only one as autoreplace can't handle mixed cargo articulated vehicles)
    # foo,
    # railbuses
    # foo,
    # diesel railcars
    # foo,
    # electric railcars
    "emu_ibex_2",
    "emu_ibex_3",
    "emu_ibex_4",
    "emu_ibex_5",
    "emu_ibex_6",
    # express electric railcars
    # foo,
    # high speed pax
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
# these can delegate to another module for reuse of wagons; this is not a common case, but used for things like torpedo cars
# explicit wagon module lists per roster are better;
# implicit modules lists were tried (just using global_constants list and allowing failing imports), but was no less maintenance, and was faff
wagon_module_names_with_roster_ids = {
    "acid_tank_cars_type_1": "pony",
    "acid_tank_cars_type_2": "pony",
    "acid_tank_cars_randomised": "pony",
    "carbon_black_hopper_cars": "pony",
    "cement_silo_cars_type_1": "pony",
    "coil_cars_covered": "pony",
    "coil_cars_covered_asymmetric": "pony",
    "coil_cars_tarpaulin": "pony",
    "coil_cars_uncovered": "pony",
    "cryo_tank_cars": "pony",
    "drop_end_flat_cars": "pony",
    "drop_side_flat_cars": "pony",
    "express_intermodal_cars": "pony",
    "flat_cars": "pony",
    "flat_cars_randomised": "pony",
    "heavy_duty_dump_cars": "pony",
    "heavy_duty_flat_cars": "pony",
    "ingot_cars": "pony",
    "intermodal_cars": "pony",
    "kaolin_hopper_cars": "pony",
    "log_cars": "pony",
    "low_floor_intermodal_cars": "pony",
    "merchandise_box_cars": "pony",
    "pipe_cars": "pony",
    "pressure_tank_cars": "pony",
    "product_tank_cars_type_1": "pony",
    "reefer_cars_type_1": "pony",
    "reefer_cars_type_2": "pony",
    "side_door_hopper_cars": "pony",
    "silo_cars_type_1": "pony",
    "slag_ladle_cars": "pony",
    "sliding_roof_cars": "pony",
    "sliding_wall_cars_type_1": "pony",
    "sliding_wall_cars_type_2": "pony",
    "tank_cars_type_1": "pony",
    "tarpaulin_cars_type_1": "pony",
    "tarpaulin_cars_type_2": "pony",
    "tarpaulin_cars_type_3": "pony",
    "tarpaulin_cars_randomised": "pony",
    "torpedo_cars": "pony",
}


def main():
    return Roster(
        id="ibex",
        numeric_id=3,
        grf_name="iron-ibex",
        grfid=r"CA\12\21",
        str_grf_name="Iron Ibex",
        # ELRL, ELNG is mapped to RAIL, NG etc
        # default intro dates per generation, can be over-ridden if needed by setting intro_year kw on model def
        intro_years={
            "RAIL": [1885, 1912, 1939, 1966, 1993, 2020],
            "METRO": [1900, 1950, 2000],
            "NG": [1860, 1905, 1950, 2000],
        },
        # default speeds per generation, can be over-ridden if needed by setting speed kw arg on model def
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
