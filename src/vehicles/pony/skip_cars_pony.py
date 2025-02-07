from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="HopperCarSkipConsist",
        base_numeric_id=6120,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, skips are slow eh?
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="empty_8px", repeat=2
    )

    # model_def.define_unit(class_name="FreightCar", chassis="empty_8px")

    result.append(model_def)

    return result
