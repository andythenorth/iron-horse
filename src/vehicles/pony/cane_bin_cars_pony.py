from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="CaneBinCar",
        base_numeric_id=1020,
        gen=1,
        subtype="U",
        base_track_type="NG",
        speed=35,  # note rare non-standard speed, bins are slow eh?
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="BinCarUnit", chassis="empty_8px")

    model_def.add_unit_def(unit_cls_name="BinCarUnit", chassis="empty_8px")

    result.append(model_def)

    return result
