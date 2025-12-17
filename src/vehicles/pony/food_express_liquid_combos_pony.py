from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="FoodExpressLiquidCombos",
        base_numeric_id=31380,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressLiquidCombos",
        base_numeric_id=31950,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressLiquidCombos",
        base_numeric_id=31970,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressLiquidCombos",
        base_numeric_id=31980,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressLiquidCombos",
        base_numeric_id=31990,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressLiquidCombos",
        base_numeric_id=32000,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FoodExpressLiquidCombos",
        base_numeric_id=32010,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
