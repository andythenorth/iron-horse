from train import CoveredHopperCarRollerRoofConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    """
    consist = CoveredHopperCarRollerRoofConsist(
        roster_id="pony",
        base_numeric_id=6890,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarRollerRoofConsist(
        roster_id="pony",
        base_numeric_id=6900,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarRollerRoofConsist(
        roster_id="pony",
        base_numeric_id=6910,
        gen=6,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")
    """
    consist = CoveredHopperCarRollerRoofConsist(
        roster_id="pony",
        base_numeric_id=6920,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")
