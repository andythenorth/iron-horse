from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20640,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20650,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20660,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20670,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20680,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20690,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20700,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="TankCarChemicalRandomisedConsist",
        base_numeric_id=20720,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_type_factory)

    return result
