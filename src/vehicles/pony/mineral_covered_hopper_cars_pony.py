from train import CoveredHopperCarMineralConsist, FreightCar


def main():
    # --------------- standard gauge ---------------------------------------------------------------

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=15990,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=16000,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=16010,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=16020,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=16070,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=16030,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = CoveredHopperCarMineralConsist(
        roster_id="pony",
        base_numeric_id=16040,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_half_filled_greebled_32px")
