from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="IntermodalCarUnit",
        base_numeric_id=28350,
        gen=3,
        intro_year_offset=15,  # let's be a little bit later for this one
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IntermodalCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="IntermodalCarUnit",
        base_numeric_id=28360,
        gen=3,
        intro_year_offset=15,  # let's be a little bit later for this one
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IntermodalCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="IntermodalCarUnit",
        base_numeric_id=28370,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IntermodalCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="IntermodalCarUnit",
        base_numeric_id=28380,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IntermodalCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="IntermodalCarUnit",
        base_numeric_id=28390,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IntermodalCarUnit", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="IntermodalCarUnit",
        base_numeric_id=28400,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IntermodalCarUnit", chassis="2_axle_1cc_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="IntermodalCarUnit",
        base_numeric_id=28410,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IntermodalCarUnit", chassis="4_axle_1cc_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="IntermodalCarUnit",
        base_numeric_id=28420,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IntermodalCarUnit", chassis="4_axle_1cc_filled_32px")

    result.append(model_def)

    return result
