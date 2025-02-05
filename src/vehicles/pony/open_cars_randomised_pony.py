from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=25560,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=25570,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=19950,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=19930,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    # no new type A for gen 2, gen 1 type A continues

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=16990,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=17000,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=17010,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=17020,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=17040,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="OpenCarRandomisedConsist",
        base_numeric_id=17050,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_type_factory)

    return result
