from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="ExpressFoodTankCarRandomisedConsist",
        base_numeric_id=28160,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="ExpressFoodTankCarRandomisedConsist",
        base_numeric_id=28170,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_type_factory)

    return result
