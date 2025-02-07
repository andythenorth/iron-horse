from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRollerRoofRandomisedConsist",
        base_numeric_id=24650,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRollerRoofRandomisedConsist",
        base_numeric_id=24670,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRollerRoofRandomisedConsist",
        base_numeric_id=24690,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRollerRoofRandomisedConsist",
        base_numeric_id=24710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    return result
