from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="TankCarStandardType2",
        base_numeric_id=33310,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarStandardType2",
        base_numeric_id=33330,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarStandardType2",
        base_numeric_id=33350,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarStandardType2",
        base_numeric_id=28950,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_sparse_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarStandardType2",
        base_numeric_id=28970,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_sparse_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TankCarStandardType2",
        base_numeric_id=30830,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_def)

    return result
