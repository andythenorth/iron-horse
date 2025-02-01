from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26700,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17760,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_sparse_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17780,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_sparse_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17700,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25040,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17300,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25020,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28320,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_gapped_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17720,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30850,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17680,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31860,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_sparse_greebled_alt_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=36240,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_sparse_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="TankCarStandardConsistType1",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25060,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(consist_factory)

    return result
