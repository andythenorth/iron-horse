from train import CoilCarCoveredConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # start gen 4, B and C lengths only

    consist = CoilCarCoveredConsist(
        roster_id="pony",
        base_numeric_id=12550,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = CoilCarCoveredConsist(
        roster_id="pony",
        base_numeric_id=12560,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = CoilCarCoveredConsist(
        roster_id="pony",
        base_numeric_id=12570,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = CoilCarCoveredConsist(
        roster_id="pony",
        base_numeric_id=12580,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = CoilCarCoveredConsist(
        roster_id="pony",
        base_numeric_id=12590,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_2cc_filled_24px")

    consist = CoilCarCoveredConsist(
        roster_id="pony",
        base_numeric_id=12600,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_2cc_filled_32px")
