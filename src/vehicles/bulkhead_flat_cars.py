from train import FlatCarBulkheadConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=14160,
        gen=2,
        subtype="U",
        base_track_type="NG",
        intro_date_offset=20,  # these are pushed right back to line up with standard gauge versions
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=14170,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=14180,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13740,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13750,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13760,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13770,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13780,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13790,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13800,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_24px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13810,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13820,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_24px")

    consist = FlatCarBulkheadConsist(
        roster_id="pony",
        base_numeric_id=13830,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_1cc_filled_32px")
