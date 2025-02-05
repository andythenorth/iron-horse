from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """

    model_type_factory =ModelTypeFactory(
        class_name="FoodHopperCarConsistType3",
        base_numeric_id=23480,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_type_factory)


    model_type_factory =ModelTypeFactory(
        class_name="FoodHopperCarConsistType3",
        base_numeric_id=23770,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_24px")

    result.append(model_type_factory)


    model_type_factory =ModelTypeFactory(
        class_name="FoodHopperCarConsistType3",
        base_numeric_id=24000,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_type_factory)


    model_type_factory =ModelTypeFactory(
        class_name="FoodHopperCarConsistType3",
        base_numeric_id=23430,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="2_axle_gapped_24px")

    result.append(model_type_factory)
    """

    model_type_factory = ModelTypeFactory(
        class_name="FoodHopperCarConsistType3",
        base_numeric_id=34200,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FoodHopperCarConsistType3",
        base_numeric_id=35070,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FoodHopperCarConsistType3",
        base_numeric_id=33040,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_chute_greebled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="FoodHopperCarConsistType3",
        base_numeric_id=36970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_chute_greebled_alt_32px"
    )

    result.append(model_type_factory)

    return result
