from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 5 start, only B and C lengths

    model_def = ModelTypeFactory(
        class_name="TarpaulinCarConsistType3",
        base_numeric_id=25750,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="TarpaulinCarConsistType3",
        base_numeric_id=27230,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    return result
