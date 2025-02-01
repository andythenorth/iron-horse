from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType3",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22170,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType3",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22180,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType3",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22190,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType3",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22200,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType3",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22210,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hopppers_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType3",
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=22220,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(consist_factory)

    return result
