from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="FoodExpressTankCarRandomised",
        base_numeric_id=27940,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressTankCarRandomised",
        base_numeric_id=27960,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
