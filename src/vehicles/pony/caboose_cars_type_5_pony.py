from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CabooseCarType5",
        base_numeric_id=16490,
        gen=1,
        subtype="aA",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_caboose_12px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType5",
        base_numeric_id=16460,
        gen=1,
        subtype="aB",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_caboose_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType5",
        base_numeric_id=16550,
        gen=1,
        subtype="aC",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="4_axle_caboose_24px")

    result.append(model_def)

    return result
