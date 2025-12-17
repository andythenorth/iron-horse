from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="BulkOpenCarAggregateType3",
        base_numeric_id=32060,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BulkOpenCarAggregateType3",
        base_numeric_id=32070,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="4_axle_sparse_32px")

    result.append(model_def)

    return result
