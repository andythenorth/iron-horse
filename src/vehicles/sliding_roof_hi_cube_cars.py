from train import FlatCarSlidingRoofConsistHiCube, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = FlatCarSlidingRoofConsistHiCube(
        roster_id="pony",
        base_numeric_id=15120,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = FlatCarSlidingRoofConsistHiCube(
        roster_id="pony",
        base_numeric_id=15920,
        gen=5,
        subtype="C",
        sprites_complete=15330,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_32px")
