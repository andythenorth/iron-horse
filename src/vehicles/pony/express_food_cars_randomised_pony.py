from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="ExpressFoodCarRandomisedConsist",
        base_numeric_id=31380,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodCarRandomisedConsist",
        base_numeric_id=31950,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodCarRandomisedConsist",
        base_numeric_id=31960,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodCarRandomisedConsist",
        base_numeric_id=31970,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodCarRandomisedConsist",
        base_numeric_id=31980,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodCarRandomisedConsist",
        base_numeric_id=31990,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodCarRandomisedConsist",
        base_numeric_id=32000,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodCarRandomisedConsist",
        base_numeric_id=32010,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
