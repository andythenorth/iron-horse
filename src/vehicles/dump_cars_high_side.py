from train import DumpCarHighSideConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=16340,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=15130,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=12630,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=18910,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=18930,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=18950,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=18970,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=18990,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=19010,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=19030,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_greebled_24px")

    consist = DumpCarHighSideConsist(
        roster_id="pony",
        base_numeric_id=19050,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_greebled_32px")
