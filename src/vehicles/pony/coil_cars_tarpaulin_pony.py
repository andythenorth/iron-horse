from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 5 start, only B and C lengths

    model_def = ModelDef(
        class_name="CoilCarTarpaulinConsist",
        base_numeric_id=26300,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_1cc_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarTarpaulinConsist",
        base_numeric_id=26400,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_1cc_filled_32px")

    result.append(model_def)

    return result
