from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="HopperCarOreType3",
        base_numeric_id=28840,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarOreType3",
        base_numeric_id=28880,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarOreType3",
        base_numeric_id=29520,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarOreType3",
        base_numeric_id=28860,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_chute_greebled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarOreType3",
        base_numeric_id=28980,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_chute_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarOreType3",
        base_numeric_id=29680,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_chute_greebled_alt_32px"
    )

    result.append(model_def)

    return result
