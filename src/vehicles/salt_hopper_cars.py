from train import HopperCarSaltConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6780,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6790,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6800,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6810,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6820,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6830,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6840,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6850,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6860,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6870,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = HopperCarSaltConsist(
        roster_id="pony",
        base_numeric_id=6880,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")
