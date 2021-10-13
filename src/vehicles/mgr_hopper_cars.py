from train import HopperCarMGRConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    # just type gen 4 and 5

    consist = HopperCarMGRConsist(
        roster_id="pony",
        base_numeric_id=6450,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = HopperCarMGRConsist(
        roster_id="pony",
        base_numeric_id=6460,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_24px")

    consist = HopperCarMGRConsist(
        roster_id="pony",
        base_numeric_id=6470,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = HopperCarMGRConsist(
        roster_id="pony",
        base_numeric_id=6480,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    # no gen 6 don't bother
