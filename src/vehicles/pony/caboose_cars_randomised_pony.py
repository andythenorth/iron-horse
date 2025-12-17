from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CabooseCarRandomised",
        base_numeric_id=32410,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="empty_8px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarRandomised",
        base_numeric_id=33440,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="empty_16px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CabooseCarRandomised",
        base_numeric_id=29310,
        gen=1,
        subtype="aA",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="empty_12px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarRandomised",
        base_numeric_id=32430,
        gen=1,
        subtype="aB",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="CabooseCarRandomised",
        base_numeric_id=33460,
        gen=1,
        subtype="aC",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CabooseCarUnit", chassis="empty_24px")

    result.append(model_def)

    return result
