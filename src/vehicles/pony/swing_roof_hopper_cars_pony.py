from train import CoveredHopperCarSwingRoofConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = CoveredHopperCarSwingRoofConsist(
        roster_id="pony",
        base_numeric_id=16100,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_hoppers_24px")

    consist = CoveredHopperCarSwingRoofConsist(
        roster_id="pony",
        base_numeric_id=16660,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")
