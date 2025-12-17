from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 5 start, only B and C lengths

    model_def = ModelDef(
        schema_name="TarpaulinCarType2",
        base_numeric_id=24850,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="TarpaulinCarType2",
        base_numeric_id=25300,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
