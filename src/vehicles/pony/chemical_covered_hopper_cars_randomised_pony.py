from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarSaltRandomisedConsist",
        base_numeric_id=24310,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarSaltRandomisedConsist",
        base_numeric_id=24340,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="empty_32px")

    result.append(model_def)

    return result
