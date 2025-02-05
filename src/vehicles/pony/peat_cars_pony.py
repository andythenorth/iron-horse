from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="PeatCarConsist",
        base_numeric_id=15170,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, bins are slow eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="BinCar", chassis="empty_8px")

    model_type_factory.define_unit(class_name="BinCar", chassis="empty_8px")

    result.append(model_type_factory)

    return result
