from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="ExpressFoodTankCarRandomised",
        base_numeric_id=28160,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="ExpressFoodTankCarRandomised",
        base_numeric_id=28170,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
