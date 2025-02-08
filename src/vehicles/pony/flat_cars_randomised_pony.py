from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- pony NG -------------------------------------------------------------------

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20820,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20830,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20840,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20850,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20860,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20870,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20880,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20890,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20900,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20910,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20920,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FlatCarRandomisedConsist",
        base_numeric_id=20930,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
