from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=35230,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=35050,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=34480,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------
    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=34810,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=34300,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=34460,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=34270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=34440,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=34250,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        chassis="empty_32px",
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=34230,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=20350,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarAggregateRandomisedConsist",
        base_numeric_id=21970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
