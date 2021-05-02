from train import AutomobileLowFloorCarConsist, AutomobileCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    # intro gen 4

    consist = AutomobileLowFloorCarConsist(
        roster_id="pony", base_numeric_id=5850, gen=4, subtype="B"
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_filled_greebled_24px")

    consist = AutomobileLowFloorCarConsist(
        roster_id="pony", base_numeric_id=5860, gen=4, subtype="C"
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")
    consist = AutomobileLowFloorCarConsist(
        roster_id="pony", base_numeric_id=5870, gen=5, subtype="B"
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_filled_greebled_24px")

    consist = AutomobileLowFloorCarConsist(
        roster_id="pony", base_numeric_id=5880, gen=5, subtype="C"
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")

    consist = AutomobileLowFloorCarConsist(
        roster_id="pony", base_numeric_id=5890, gen=6, subtype="B"
    )

    consist.add_unit(type=AutomobileCar, chassis="2_axle_filled_greebled_24px")

    consist = AutomobileLowFloorCarConsist(
        roster_id="pony", base_numeric_id=5900, gen=6, subtype="C"
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")
