from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="SpacerCabbageCarType2",
        base_numeric_id=33380,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SpacerCarUnit", chassis="2_axle_ng_8px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SpacerCabbageCarType2",
        base_numeric_id=36190,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SpacerCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="SpacerCabbageCarType2",
        base_numeric_id=32450,
        gen=1,
        subtype="aA",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SpacerCarUnit", chassis="2_axle_caboose_12px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SpacerCabbageCarType2",
        base_numeric_id=32460,
        gen=1,
        subtype="aB",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SpacerCarUnit", chassis="2_axle_caboose_16px")

    result.append(model_def)

    # 5/8 length tried, not needed

    model_def = ModelDef(
        class_name="SpacerCabbageCarType2",
        base_numeric_id=31780,
        gen=1,
        subtype="aC",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SpacerCarUnit", chassis="4_axle_caboose_24px")

    result.append(model_def)

    return result
