from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=26370,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=33000,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=30610,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="3_axle_solid_express_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=31060,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=31810,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="3_axle_solid_express_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=31960,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=32090,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=34610,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="LivestockExpressCar",
        base_numeric_id=32130,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(model_def)

    return result
