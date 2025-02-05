from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 5 start, only B and C lengths

    model_type_factory = ModelTypeFactory(
        class_name="TarpaulinCarConsistType2",
        base_numeric_id=24850,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TarpaulinCarConsistType2",
        base_numeric_id=24980,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_type_factory)

    return result
