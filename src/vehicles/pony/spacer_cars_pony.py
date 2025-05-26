from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    """
    model_def = ModelDef(
        class_name="SpacerCar",
        base_numeric_id=23690,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_ng_8px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SpacerCar",
        base_numeric_id=26270,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)
    """
    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="SpacerCar",
        base_numeric_id=36630,
        gen=1,
        subtype="Z",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_caboose_12px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SpacerCar",
        base_numeric_id=38790,
        gen=1,
        subtype="A",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_caboose_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SpacerCar",
        base_numeric_id=36190,
        gen=1,
        subtype="Y",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_caboose_20px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SpacerCar",
        base_numeric_id=33380,
        gen=1,
        subtype="B",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_caboose_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SpacerCar",
        base_numeric_id=31780,
        gen=1,
        subtype="X",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="2_axle_caboose_28px")

    result.append(model_def)


    """
    model_def = ModelDef(
        class_name="SpacerCar",
        base_numeric_id=23280,
        gen=1,
        subtype="B",
        docs_image_spriterow=3,
        sprites_complete=False,
    )

    model_def.add_unit_def(class_name="CabooseCarUnit", chassis="4_axle_caboose_24px")

    result.append(model_def)
    """
    return result
