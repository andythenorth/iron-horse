from train import DumpCarConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    # gen 2 start for dump cars eh?
    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=4020,
        gen=2,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=30,
        gen=3,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=40,
        gen=4,
        subtype="U",
        base_track_type="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=2960,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=2350,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=2360,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=2370,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=2380,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    # no gen 5A or 6A

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=1810,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=2110,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=2400,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = DumpCarConsist(
        roster_id="pony",
        base_numeric_id=2390,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")
