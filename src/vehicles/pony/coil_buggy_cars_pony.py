from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="CoilBuggyCarConsist",
        base_numeric_id=5160,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill coils eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="CoilBuggyCar", chassis="empty_8px", repeat=2
    )

    result.append(model_type_factory)

    return result
