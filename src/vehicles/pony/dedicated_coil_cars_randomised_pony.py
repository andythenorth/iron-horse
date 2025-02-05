from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="DedicatedCoilCarRandomisedConsist",
        base_numeric_id=25860,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="DedicatedCoilCarRandomisedConsist",
        base_numeric_id=25870,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="DedicatedCoilCarRandomisedConsist",
        base_numeric_id=25880,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="empty_32px",
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="DedicatedCoilCarRandomisedConsist",
        base_numeric_id=25890,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="DedicatedCoilCarRandomisedConsist",
        base_numeric_id=25900,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_type_factory)

    return result
