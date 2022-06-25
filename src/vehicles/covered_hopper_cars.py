from train import CoveredHopperCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13320,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13340,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13350,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13370,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13380,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13390,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13400,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = CoveredHopperCarConsist(
        roster_id="pony",
        base_numeric_id=13410,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
