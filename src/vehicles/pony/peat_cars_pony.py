from train.train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="PeatCarConsist",
        base_numeric_id=15170,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, bins are slow eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="BinCar", chassis="empty_8px")

    model_def.add_unit_def(class_name="BinCar", chassis="empty_8px")

    result.append(model_def)

    return result
