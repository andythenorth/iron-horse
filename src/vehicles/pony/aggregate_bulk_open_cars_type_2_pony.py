from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="BulkOpenCarAggregateType2",
        base_numeric_id=28500,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BulkOpenCarAggregateType2",
        base_numeric_id=28510,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_32px")

    result.append(model_def)

    return result
