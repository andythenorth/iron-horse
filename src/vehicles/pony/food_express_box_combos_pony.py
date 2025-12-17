from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="FoodExpressBoxCombos",
        base_numeric_id=30720,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressBoxCombos",
        base_numeric_id=30700,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressBoxCombos",
        base_numeric_id=35420,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressBoxCombos",
        base_numeric_id=35430,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressBoxCombos",
        base_numeric_id=35440,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressBoxCombos",
        base_numeric_id=36000,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressBoxCombos",
        base_numeric_id=36010,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressBoxCombos",
        base_numeric_id=36020,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
