from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    consist_factory = ConsistFactory(
        class_name="BoxCarRandomisedConsist",
        base_numeric_id=31330,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarRandomisedConsist",
        base_numeric_id=31340,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BoxCarRandomisedConsist",
        base_numeric_id=16680,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarRandomisedConsist",
        base_numeric_id=16690,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarRandomisedConsist",
        base_numeric_id=16700,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarRandomisedConsist",
        base_numeric_id=16710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarRandomisedConsist",
        base_numeric_id=16720,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
