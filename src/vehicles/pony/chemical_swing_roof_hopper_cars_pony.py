from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarSaltSwingRoofConsist",
        base_numeric_id=27260,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_1cc_filled_hoppers_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarSaltSwingRoofConsist",
        base_numeric_id=22060,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(model_def)

    return result
