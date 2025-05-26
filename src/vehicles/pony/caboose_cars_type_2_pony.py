from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="CabooseCarType2",
        base_numeric_id=38960,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_ng_8px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CabooseCarType2",
        base_numeric_id=38970,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="CabooseCarType2",
        base_numeric_id=38980,
        gen=1,
        subtype="A",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_caboose_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CabooseCarType2",
        base_numeric_id=38990,
        gen=1,
        subtype="B",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="4_axle_caboose_24px")

    result.append(model_def)

    return result
