from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19750,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19770,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19790,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------
    # also just type A for gen 1, 2 and 3

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19570,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    # gen 1A also covers gen 2

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19590,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19610,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19630,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19650,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19670,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19690,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarHighSide",
        base_numeric_id=19730,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    return result
