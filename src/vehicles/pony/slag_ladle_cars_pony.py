from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="SlagLadleCarUnit",
        base_numeric_id=24030,
        gen=1,
        subtype="U",
        base_track_type="NG",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SlagLadleCarUnit", chassis="buffers_only_16px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="SlagLadleCarUnit",
        base_numeric_id=23410,
        gen=1,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SlagLadleCarUnit", chassis="buffers_only_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SlagLadleCarUnit",
        base_numeric_id=23420,
        gen=4,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill molten slag eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="SlagLadleCarUnit", chassis="buffers_only_16px")

    result.append(model_def)

    return result
