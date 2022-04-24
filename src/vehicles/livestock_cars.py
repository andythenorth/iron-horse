from train import LivestockCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=1030,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=620,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=680,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=1010,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no gen 2 needed

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=2680,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=1020,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=2720,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_2cc_filled_32px")

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=7160,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=2,
    )

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=2710,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_2cc_filled_32px")

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=7170,
        gen=6,
        subtype="D",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=2,
    )
