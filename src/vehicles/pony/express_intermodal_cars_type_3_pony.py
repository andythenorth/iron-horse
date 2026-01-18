from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # only gen 5 and 6 eh

    model_def = ModelDef(
        schema_name="ExpressIntermodalCarType3",
        base_numeric_id=16900,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressIntermodalCarUnit", chassis="2_axle_2cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="ExpressIntermodalCarType3",
        base_numeric_id=16940,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressIntermodalCarUnit", chassis="4_axle_2cc_filled_32px"
    )

    result.append(model_def)

    return result
