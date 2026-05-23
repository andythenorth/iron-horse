from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="HopperCarCoalType3",
        base_numeric_id=29720,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarCoalType3",
        base_numeric_id=29800,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarCoalType3",
        base_numeric_id=29840,
        gen=5,
        subtype="A",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarCoalType3",
        base_numeric_id=30560,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarCoalType3",
        base_numeric_id=30740,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    return result
