from train import AutomobileCarConsist, AutomobileCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = AutomobileCarConsist(
        roster_id="pony", base_numeric_id=5710, gen=5, subtype="B"
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_filled_greebled_24px")

    consist = AutomobileCarConsist(
        roster_id="pony", base_numeric_id=5720, gen=5, subtype="C"
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")
