from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # only gen 5 and 6 eh

    model_def = ModelDef(
        class_name="ExpressIntermodalCar",
        base_numeric_id=22960,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressIntermodalCar", chassis="2_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressIntermodalCar",
        base_numeric_id=22970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressIntermodalCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    return result
