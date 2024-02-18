from train import DumpCarAggregateConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = DumpCarAggregateConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=14730,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    # gen 1 also covers gen 2

    consist = DumpCarAggregateConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11390,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarAggregateConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11400,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = DumpCarAggregateConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11410,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarAggregateConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11420,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = DumpCarAggregateConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=15740,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = DumpCarAggregateConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=10850,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_24px")

    consist = DumpCarAggregateConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11150,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")
