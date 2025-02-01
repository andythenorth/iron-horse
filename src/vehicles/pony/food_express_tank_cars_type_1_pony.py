from train import ConsistFactory


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    # note that NG uses FreightCar not ExpressCar, as there is no adjustment of capacity for higher speed
    # this is a bit of an inconsistency in the set design, but it's a tradeoff where the alternative is having no NG food tanker at all, or bizarrely low capacity

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19960,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=19980,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_sparse_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=20000,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_sparse_24px")

    result.append(consist_factory)

    # --------------- standard gauge ---------------------------------------------------------------
    # no gen 1 for food tank cars - straight to gen 2

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17200,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17210,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressCar", chassis="3_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17220,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressCar", chassis="3_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17230,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressCar", chassis="4_axle_sparse_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28190,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressCar", chassis="4_axle_sparse_32px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28440,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressCar", chassis="3_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16970,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressCar", chassis="4_axle_sparse_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="ExpressFoodTankCarConsistType1",
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28180,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="ExpressCar", chassis="4_axle_sparse_32px")

    result.append(consist_factory)

    return result
