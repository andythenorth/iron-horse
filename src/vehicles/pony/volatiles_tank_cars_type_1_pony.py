from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=24300,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=24330,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=24600,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_ng_sparse_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22260,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22400,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22280,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22420,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22300,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22480,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22320,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22440,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22340,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_sparse_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=22460,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_sparse_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarVolatilesType1",
        base_numeric_id=24620,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_def)

    return result
