from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="ReeferCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31930,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ReeferCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31940,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ReeferCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31920,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ReeferCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31900,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ReeferCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31910,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ReeferCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23060,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ReeferCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23070,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
