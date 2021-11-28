from train import CoveredHopperCarMineralConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=6950,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=6960,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=6970,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=6980,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=7030,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=6990,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=7000,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_greebled_32px") # extra pixels drawn in manually on wagon sprite for appearance

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=7010,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=7020,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_greebled_32px") # extra pixels drawn in manually on wagon sprite for appearance
