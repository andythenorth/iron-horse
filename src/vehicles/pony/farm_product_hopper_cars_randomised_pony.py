from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="FarmProductsHopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19870,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsHopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30320,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsHopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16980,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsHopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30290,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsHopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17280,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsHopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17360,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsHopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18540,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsHopperCarRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30390,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
