from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="TorpedoCarConsist",
        base_numeric_id=4140,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=6)

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TorpedoCarConsist",
        base_numeric_id=4060,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=6)

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TorpedoCarConsist",
        base_numeric_id=4170,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=6)

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TorpedoCarConsist",
        base_numeric_id=4090,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=6)

    model_type_factory.define_unit(class_name="TorpedoCar", vehicle_length=3)

    result.append(model_type_factory)

    return result
