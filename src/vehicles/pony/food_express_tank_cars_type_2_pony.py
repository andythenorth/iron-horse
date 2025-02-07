from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # no gen 1 for food tank cars - straight to gen 2
    """

    model_def =ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=17200,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="ExpressCar", chassis="2_axle_filled_16px")

    result.append(model_def)


    model_def =ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=17210,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="ExpressCar", chassis="3_axle_filled_16px")

    result.append(model_def)


    model_def =ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=17220,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="ExpressCar", chassis="3_axle_filled_16px")

    result.append(model_def)


    model_def =ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=17230,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="ExpressCar", chassis="4_axle_sparse_24px")

    result.append(model_def)


    model_def =ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=28190,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="ExpressCar", chassis="4_axle_sparse_32px")

    result.append(model_def)


    model_def =ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=28440,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="ExpressCar", chassis="3_axle_filled_16px")

    result.append(model_def)


    model_def =ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=16970,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="ExpressCar", chassis="4_axle_sparse_24px")

    result.append(model_def)


    model_def =ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=28180,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="ExpressCar", chassis="4_axle_sparse_32px")

    result.append(model_def)

    # gen 6A not included - could add?
    """

    model_def = ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=20380,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="ExpressCar", chassis="4_axle_sparse_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="ExpressFoodTankCarConsistType2",
        base_numeric_id=20390,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="ExpressCar", chassis="4_axle_sparse_32px"
    )

    result.append(model_def)

    return result
