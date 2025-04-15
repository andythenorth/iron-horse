from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="IngotCarUnit",
        base_numeric_id=5150,
        gen=1,
        subtype="U",
        base_track_type="NG",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IngotCarUnit", chassis="empty_8px", repeat=2)

    result.append(model_def)

    # --------------- pony -------------------------------------------------------------------------

    model_def = ModelDef(
        class_name="IngotCarUnit",
        base_numeric_id=80,
        gen=1,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IngotCarUnit", chassis="empty_8px", repeat=2)

    result.append(model_def)

    model_def = ModelDef(
        class_name="IngotCarUnit",
        base_numeric_id=60,
        gen=4,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="IngotCarUnit", chassis="empty_8px", repeat=2)

    result.append(model_def)

    return result
