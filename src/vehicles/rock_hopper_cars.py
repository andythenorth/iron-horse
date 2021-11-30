from train import HopperCarRockConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=2310,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=1070,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=2330,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=1080,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=2000,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=2010,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=1610,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=1600,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hopppers_24px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=1620,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=2020,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hopppers_24px")

    consist = HopperCarRockConsist(
        roster_id="pony",
        base_numeric_id=1990,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_hoppers_32px")
