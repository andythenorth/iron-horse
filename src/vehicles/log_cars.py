from train import LogCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=7180,
        gen=1,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_spine_16px")

    # no gen 2 for NG, straight to gen 3

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=7190,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_spine_16px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=7200,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_spine_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=2740,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=2730,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=2750,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=1710,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=2760,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=1930,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=2770,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = LogCarConsist(
        roster_id="pony", base_numeric_id=930, gen=5, subtype="C", sprites_complete=True
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=1910,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    consist = LogCarConsist(
        roster_id="pony",
        base_numeric_id=1920,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_2cc_filled_32px")
