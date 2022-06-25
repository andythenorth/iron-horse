from train import HopperCarRockConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=11350,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=10110,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=11370,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=10120,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=11040,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=11050,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=10650,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=10640,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hopppers_24px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=10660,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=11060,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hopppers_24px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=11030,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")
