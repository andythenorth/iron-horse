from train import CoveredHopperCarRollerRoofConsist, FreightCar


def main(roster_id):
    # --------------- narrow gauge -----------------------------------------------------------------

    consist = CoveredHopperCarRollerRoofConsist(
        roster_id=roster_id,
        base_numeric_id=16270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarRollerRoofConsist(
        roster_id=roster_id,
        base_numeric_id=16840,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarRollerRoofConsist(
        roster_id=roster_id,
        base_numeric_id=16120,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = CoveredHopperCarRollerRoofConsist(
        roster_id=roster_id,
        base_numeric_id=17160,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")
