from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="BulkOpenCarTipplerType3",
        base_numeric_id=16470,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BulkOpenCarTipplerType3",
        base_numeric_id=29700,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_greebled_32px"
    )

    result.append(model_def)

    return result
