from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28340,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=16920,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=17030,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28240,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28250,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28260,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28280,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=22140,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28290,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkCarMixedRandomisedConsist",
        base_numeric_id=28300,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
