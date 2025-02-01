from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32310,
        gen=2,
        subtype="A",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28530,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=32330,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22360,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28550,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28570,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28590,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28610,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28630,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarProductRandomisedConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=36370,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(consist_factory)

    return result
