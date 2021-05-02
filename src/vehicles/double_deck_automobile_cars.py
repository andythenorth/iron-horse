from train import AutomobileDoubleDeckCarConsist, AutomobileCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    # intro gen 4

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony", base_numeric_id=5790, gen=4, subtype="B"
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_filled_greebled_24px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony", base_numeric_id=5800, gen=4, subtype="C"
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")
    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony", base_numeric_id=5810, gen=5, subtype="B"
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_filled_greebled_24px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony", base_numeric_id=5820, gen=5, subtype="C"
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony", base_numeric_id=5830, gen=6, subtype="B"
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_filled_greebled_24px")

    consist = AutomobileDoubleDeckCarConsist(
        roster_id="pony", base_numeric_id=5840, gen=6, subtype="C"
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")
