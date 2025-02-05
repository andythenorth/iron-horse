from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="CoveredHopperCarSwingRoofConsist",
        base_numeric_id=26200,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_1cc_filled_hoppers_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="CoveredHopperCarSwingRoofConsist",
        base_numeric_id=16660,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(model_type_factory)

    return result
