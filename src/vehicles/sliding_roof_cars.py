from train import FlatCarSlidingRoofConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = FlatCarSlidingRoofConsist(
        roster_id="pony",
        base_numeric_id=14270,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    consist = FlatCarSlidingRoofConsist(
        roster_id="pony",
        base_numeric_id=14280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    consist = FlatCarSlidingRoofConsist(
        roster_id="pony",
        base_numeric_id=14260,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    consist = FlatCarSlidingRoofConsist(
        roster_id="pony",
        base_numeric_id=14250,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    # --------------- ibex ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = FlatCarSlidingRoofConsist(
        roster_id="ibex",
        base_numeric_id=8690,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    consist = FlatCarSlidingRoofConsist(
        roster_id="ibex",
        base_numeric_id=8700,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

    consist = FlatCarSlidingRoofConsist(
        roster_id="ibex",
        base_numeric_id=8710,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    consist = FlatCarSlidingRoofConsist(
        roster_id="ibex",
        base_numeric_id=8720,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
