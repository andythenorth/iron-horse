from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=29000,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=30280,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=30430,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------
    # only type A for gen 1

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=34270,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=38620,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="3_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=23020,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=38640,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=23040,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=38660,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=39930,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_filled_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=34800,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_filled_greebled_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarMillType1",
        base_numeric_id=39950,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
