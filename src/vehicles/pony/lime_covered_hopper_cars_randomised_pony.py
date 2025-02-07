from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeRandomisedConsist",
        base_numeric_id=24750,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeRandomisedConsist",
        base_numeric_id=26610,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeRandomisedConsist",
        base_numeric_id=26620,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeRandomisedConsist",
        base_numeric_id=26630,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeRandomisedConsist",
        base_numeric_id=26640,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
