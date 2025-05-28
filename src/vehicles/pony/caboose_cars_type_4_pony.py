from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    # really can't find 4 meaningful variants at 2/8

    model_def = ModelDef(
        class_name="CabooseCarType4",
        base_numeric_id=29270,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="CabooseCarType4",
        base_numeric_id=29370,
        gen=1,
        subtype="aA",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_caboose_12px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CabooseCarType4",
        base_numeric_id=29130,
        gen=1,
        subtype="aB",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_caboose_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="CabooseCarType4",
        base_numeric_id=29290,
        gen=1,
        subtype="aC",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="4_axle_caboose_24px")

    result.append(model_def)

    return result
