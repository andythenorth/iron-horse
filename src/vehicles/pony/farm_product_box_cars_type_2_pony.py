from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- pony --------------------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=35450,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=35460,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="3_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=35470,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=35480,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="3_axle_gapped_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=35300,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=35600,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_filled_24px")

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=35120,
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
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=28430,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_24px"
    )

    result.append(consist_factory)

    consist_factory = ConsistFactory(
        class_name="FarmProductsBoxCarConsistType2",
        base_numeric_id=32960,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(consist_factory)

    return result
