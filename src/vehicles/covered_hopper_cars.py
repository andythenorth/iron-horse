from train import CoveredHopperCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=4280,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=4300,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=4310,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=4330,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=4340,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=4350,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=4360,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=4370,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
