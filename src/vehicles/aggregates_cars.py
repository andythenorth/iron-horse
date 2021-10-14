from train import DumpCarAggregatesConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=5690,
        gen=1,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    # gen 1 also covers gen 2

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=2350,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=2360,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=2370,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=2380,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=6700,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=1810,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_24px")

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=2110,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=2400,
        gen=6,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_greebled_24px")

    consist = DumpCarAggregatesConsist(
        roster_id="pony",
        base_numeric_id=2390,
        gen=6,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_greebled_32px")
