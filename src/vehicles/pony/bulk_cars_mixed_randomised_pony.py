from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28340,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=16920,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=17030,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28240,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    # no new type A for gen 2, gen 1 type A continues

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28250,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28260,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28280,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=22140,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28290,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28300,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
