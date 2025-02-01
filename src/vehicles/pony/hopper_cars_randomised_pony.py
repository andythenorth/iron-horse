from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23900,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23910,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23920,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23930,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    # no new type A for gen 2, gen 1 type A continues

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23940,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23950,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16890,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16900,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16910,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23960,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16930,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="HopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16940,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
