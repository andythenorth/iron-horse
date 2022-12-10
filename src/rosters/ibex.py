import global_constants

from roster import Roster

from vehicles import ae_3_5
from vehicles import ae_3_6_1
from vehicles import ae_4_7
from vehicles import bb_7200
from vehicles import bb_8100_duo
from vehicles import bb_8500_duo
from vehicles import bb_22200
from vehicles import bb_22200_upgraded
from vehicles import bb_25200
from vehicles import bb_27000
from vehicles import bb_26000
from vehicles import bb_26000_upgraded
from vehicles import bls_ae_4_4
from vehicles import bls_ae_6_8
from vehicles import bls_ae_8_8
from vehicles import bls_re_4_4
from vehicles import bls_re_475
from vehicles import cc_6500
from vehicles import cc_7100
from vehicles import de_6_6
from vehicles import drg_e_16
from vehicles import emu_ibex_2
from vehicles import emu_ibex_3
from vehicles import emu_ibex_4
from vehicles import emu_ibex_5
from vehicles import emu_ibex_6
from vehicles import fs_e330
from vehicles import fs_e412
from vehicles import fs_e428
from vehicles import fs_e444
from vehicles import fs_e464
from vehicles import fs_e464_upgrade
from vehicles import fs_e633
from vehicles import fs_e636
from vehicles import fs_e646
from vehicles import fs_e652
from vehicles import fs_e656
from vehicles import fs_e656_upgraded
from vehicles import high_power_railcar_2
from vehicles import high_power_railcar_3
from vehicles import high_power_railcar_4
from vehicles import high_power_railcar_5
from vehicles import hungarian_2d2_400
from vehicles import krokodil_ce_6_8
from vehicles import krokodil_be_6_8
from vehicles import mthb_re_486
from vehicles import obb_1010
from vehicles import obb_1014
from vehicles import obb_1042
from vehicles import obb_1040
from vehicles import obb_1041
from vehicles import obb_1044
from vehicles import obb_1141
from vehicles import obb_1142
from vehicles import obb_1163
from vehicles import obb_1170_2
from vehicles import obb_1570
from vehicles import plm_2cc2_3400
from vehicles import po_2d2_5500
from vehicles import re_4_4_i
from vehicles import re_430
from vehicles import re_430_lion
from vehicles import re_450
from vehicles import re_460
from vehicles import re_465
from vehicles import re_6_6
from vehicles import re_6_6_ii
from vehicles import saas_be_4_4
from vehicles import sbb_ee_6_6_ii
from vehicles import sbb_eem_923
from vehicles import sbb_fb_4_4
from vehicles import sbb_ae_4_6
from vehicles import sbb_re_4_4_ii
from vehicles import sob_re_446
from vehicles import snowplough_ibex_gen_2
from vehicles import traxx_e_494
from vehicles import trient
from vehicles import vectron_dual_mode


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
        livery_presets={
            "FOO": {
                # note the remap to yellow, allowing 1cc wagons to be whatever player chooses
                "remap_to_cc": "COLOUR_YELLOW",
                "docs_image_input_cc": [
                    ("COLOUR_YELLOW", "COLOUR_PALE_GREEN"),
                    ("COLOUR_ORANGE", "COLOUR_DARK_GREEN"),
                    ("COLOUR_ORANGE", "COLOUR_GREEN"),
                    ("COLOUR_CREAM", "COLOUR_MAUVE"),
                ],
            },
        },
        # this list is manually maintained deliberately, even though it could be mostly automated using tech tree
        engines=[
            # challenger, # for NA roster
            # branch express
            # foo,
            # express (electro-diesels with non-standard position in power/length tree)
            # foo,
            # express
            ## AC
            ae_3_5,
            sbb_fb_4_4,
            saas_be_4_4,
            obb_1040,
            sbb_eem_923,
            ae_3_6_1,
            obb_1570,
            obb_1170_2,
            re_4_4_i,
            obb_1163,
            vectron_dual_mode,
            ## DC
            hungarian_2d2_400,
            ## AC
            ae_4_7,
            obb_1041,
            obb_1141,
            re_450,
            obb_1014,
            ## DC
            fs_e330,
            fs_e428,
            fs_e444,
            fs_e464,
            fs_e464_upgrade,
            ## AC
            drg_e_16,
            obb_1010,
            obb_1042,
            obb_1142,
            fs_e412,
            ## DC
            fs_e636,
            fs_e646,
            fs_e656,
            fs_e656_upgraded,
            ## AC
            bls_ae_6_8,
            bls_ae_4_4,
            bls_re_4_4,
            sob_re_446,
            ## DC
            plm_2cc2_3400,
            cc_7100,
            bb_7200,
            bb_22200,
            bb_22200_upgraded,
            ## AC
            obb_1044,
            re_460,
            re_465,
            ## DC
            cc_6500,
            bb_26000,
            bb_26000_upgraded,
            # high powered railcars
            high_power_railcar_2,
            high_power_railcar_3,
            high_power_railcar_4,
            high_power_railcar_5,
            # driving cab cars
            # foo,
            # branch freight
            de_6_6,
            # freight
            trient,
            ## AC
            krokodil_ce_6_8,
            krokodil_be_6_8,
            sbb_ee_6_6_ii,
            mthb_re_486,
            ## DC
            po_2d2_5500,
            bb_25200,
            bb_27000,
            ## AC
            sbb_ae_4_6,
            sbb_re_4_4_ii,
            re_430,
            re_430_lion,
            ## DC
            fs_e633,
            fs_e652,
            traxx_e_494,
            ## AC
            bls_ae_8_8,
            bls_re_475,
            ## DC
            bb_8100_duo,
            bb_8500_duo,
            ## AC
            re_6_6,
            re_6_6_ii,
            ## DC
            # joker engines / snowploughs
            snowplough_ibex_gen_2,
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
            emu_ibex_2,
            emu_ibex_3,
            emu_ibex_4,
            emu_ibex_5,
            emu_ibex_6,
            ## DC
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
        ],
    )
