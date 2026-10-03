from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    """
    model_def = ModelDef(
        schema_name="GasTankCarStandardType1",
        base_numeric_id=64960,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)
    """
    model_def = ModelDef(
        schema_name="GasTankCarStandardType1",
        base_numeric_id=64950,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)
    """
    model_def = ModelDef(
        schema_name="GasTankCarStandardType1",
        base_numeric_id=64940,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="GasTankCarStandardType1",
        base_numeric_id=64930,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="GasTankCarStandardType1",
        base_numeric_id=64920,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="GasTankCarStandardType1",
        base_numeric_id=64910,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_alt_32px"
    )

    result.append(model_def)
    """
    return result
