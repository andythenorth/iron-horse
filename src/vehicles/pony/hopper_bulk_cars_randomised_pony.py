from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=16440,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=24530,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=26450,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=25670,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    # no new type A for gen 2, gen 1 type A continues

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=24490,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=24500,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=30440,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=30450,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=22150,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=30620,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarHopperRandomisedConsist",
        base_numeric_id=27280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
