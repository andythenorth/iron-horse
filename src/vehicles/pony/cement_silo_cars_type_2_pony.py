from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType2",
        base_numeric_id=23200,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType2",
        base_numeric_id=23210,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType2",
        base_numeric_id=23290,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType2",
        base_numeric_id=23300,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType2",
        base_numeric_id=23310,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hopppers_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="SiloCarCementConsistType2",
        base_numeric_id=23400,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(consist_factory)

    return result
