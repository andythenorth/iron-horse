from train import KaolinHopperCarConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = KaolinHopperCarConsist(
        roster_id="pony",
        base_numeric_id=7110,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = KaolinHopperCarConsist(
        roster_id="pony",
        base_numeric_id=7120,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = KaolinHopperCarConsist(
        roster_id="pony",
        base_numeric_id=6930,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = KaolinHopperCarConsist(
        roster_id="pony",
        base_numeric_id=6940,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")
