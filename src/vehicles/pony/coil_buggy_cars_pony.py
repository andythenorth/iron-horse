from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CoilBuggyCarUnit",
        base_numeric_id=330,
        gen=1,
        subtype="U",
        base_track_type="NG",
        speed=35,  # note rare non-standard speed, don't spill coils eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="CoilBuggyCarUnit", chassis="empty_8px", repeat=2)

    result.append(model_def)

    return result
