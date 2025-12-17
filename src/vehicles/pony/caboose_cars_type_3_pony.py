from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CabooseCarType3",
        base_numeric_id=32370,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_ng_8px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType3",
        base_numeric_id=29230,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CabooseCarType3",
        base_numeric_id=29110,
        gen=1,
        subtype="aA",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_caboose_12px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType3",
        base_numeric_id=32390,
        gen=1,
        subtype="aB",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="2_axle_caboose_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarType3",
        base_numeric_id=29250,
        gen=1,
        subtype="aC",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="4_axle_caboose_24px")

    result.append(model_def)

    return result
