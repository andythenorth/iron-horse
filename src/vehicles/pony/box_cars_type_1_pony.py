from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18480,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    # no gen 2 for NG, straight to gen 3

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18500,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=27040,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------
    # only type A for gen 1

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18400,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    # no new type A for gen 2, gen 1 type A continues

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=37050,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="3_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18380,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18460,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18340,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18420,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18440,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24250,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="BoxCarConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18360,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_1cc_filled_32px")

    result.append(consist_factory)

    return result
