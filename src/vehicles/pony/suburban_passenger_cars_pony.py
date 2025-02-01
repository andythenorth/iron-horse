from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    # no NG suburban cars in pony

    # --------------- standard gauge ---------------------------------------------------------------
    # no gen 1, the capacity difference is negligible compared to standard pax

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29900,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="3_axle_solid_express_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29910,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29920,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="3_axle_solid_express_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29930,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29940,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="6_axle_solid_express_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29950,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29960,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="4_axle_solid_express_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29970,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29980,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="4_axle_solid_express_32px")

    # gen 6 broadly same as gen 5, but new liveries (any other difference?)

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=29990,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="PassengerSuburbanCarConsist",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30120,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="4_axle_solid_express_32px")

    result.append(consist_factory)

    return result
