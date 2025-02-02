from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """

    consist_factory = ConsistFactory(
        class_name="MetalProductCarCoveredRandomisedConsist",
        base_numeric_id=25670,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    result.append(consist_factory)

    """

    consist_factory = ConsistFactory(
        class_name="MetalProductCarCoveredRandomisedConsist",
        base_numeric_id=25680,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="MetalProductCarCoveredRandomisedConsist",
        base_numeric_id=25690,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
