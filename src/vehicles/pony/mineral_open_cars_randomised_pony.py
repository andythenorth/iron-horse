from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=31690,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=31710,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=31730,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=27190,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=27210,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=31630,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=31610,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=31670,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=28200,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=28450,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="BulkOpenCarMineralRandomisedConsist",
        base_numeric_id=31650,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
