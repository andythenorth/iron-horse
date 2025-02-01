from train import ConsistFactory


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24370,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    # no gen 2 for NG, straight to gen 3

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24390,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24410,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16480,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25610,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24830,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25630,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16450,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        chassis="4_axle_filled_32px",
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25650,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        chassis="2_axle_filled_greebled_24px",
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarMerchandiseConsist",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24810,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        chassis="4_axle_filled_greebled_32px",
    )

    result.append(consist_factory)

    return result
