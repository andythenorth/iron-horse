from train import LivestockCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=18160,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # no gen 2 for NG, straight to gen 3

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=18180,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    """ # restore in next version ??
    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=18200,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")
    """
    # --------------- pony ----------------------------------------------------------------------
    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=18220,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    # no gen 2 needed

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=18240,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=18260,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = LivestockCarConsist(
        roster_id="pony",
        base_numeric_id=18280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")

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
