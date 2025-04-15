from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="HopperCarSkip",
        base_numeric_id=6120,
        gen=1,
        subtype="U",
        base_track_type="NG",
        speed=35,  # note rare non-standard speed, skips are slow eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_8px", repeat=2)

    # model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_8px")

    result.append(model_def)

    return result
