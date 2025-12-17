from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="BoxCarCurtainSideType2",
        base_numeric_id=33290,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BoxCarCurtainSideType2",
        base_numeric_id=36430,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BoxCarCurtainSideType2",
        base_numeric_id=36450,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BoxCarCurtainSideType2",
        base_numeric_id=36470,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BoxCarCurtainSideType2",
        base_numeric_id=36490,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_1cc_filled_greebled_32px"
    )

    result.append(model_def)

    return result
