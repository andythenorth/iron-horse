from train import CoveredHopperCarSwingRoofConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = CoveredHopperCarSwingRoofConsist(
        roster_id="pony",
        base_numeric_id=7060,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_hoppers_24px")

    consist = CoveredHopperCarSwingRoofConsist(
        roster_id="pony",
        base_numeric_id=7070,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")

    consist = CoveredHopperCarSwingRoofConsist(
        roster_id="pony",
        base_numeric_id=7050,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_hoppers_24px")

    consist = CoveredHopperCarSwingRoofConsist(
        roster_id="pony",
        base_numeric_id=7040,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")
