from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- metro -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=15260,
        gen=1,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_metro_16px", repeat=2
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=27770,
        gen=2,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_metro_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=22810,
        gen=3,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_metro_32px")

    result.append(model_def)

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=22830,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=22850,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=22870,
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
        schema_name="OpenCarType1",
        base_numeric_id=22890,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=29870,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="3_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=22910,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=26110,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=22930,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=26130,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=28150,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_filled_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=27570,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_filled_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=26160,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="OpenCarType1",
        base_numeric_id=27590,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
