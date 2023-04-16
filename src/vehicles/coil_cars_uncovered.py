from train import CoilCarUncoveredConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # start gen 4

    consist = CoilCarUncoveredConsist(
        roster_id="pony",
        base_numeric_id=14040,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = CoilCarUncoveredConsist(
        roster_id="pony",
        base_numeric_id=14050,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = CoilCarUncoveredConsist(
        roster_id="pony",
        base_numeric_id=14060,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = CoilCarUncoveredConsist(
        roster_id="pony",
        base_numeric_id=14070,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_24px")

    consist = CoilCarUncoveredConsist(
        roster_id="pony",
        base_numeric_id=14080,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
