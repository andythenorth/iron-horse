from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="IngotCarConsist",
        base_numeric_id=5150,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="IngotCar", chassis="empty_8px", repeat=2)

    result.append(model_type_factory)

    # --------------- pony -------------------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="IngotCarConsist",
        base_numeric_id=80,
        gen=1,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="IngotCar", chassis="empty_8px", repeat=2)

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="IngotCarConsist",
        base_numeric_id=60,
        gen=4,
        subtype="U",
        speed=35,  # note rare non-standard speed, don't spill hot ingots eh?
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="IngotCar", chassis="empty_8px", repeat=2)

    result.append(model_type_factory)

    return result
