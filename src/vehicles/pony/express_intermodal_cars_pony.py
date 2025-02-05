from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # only gen 5 and 6 eh

    model_type_factory = ModelTypeFactory(
        class_name="ExpressIntermodalCarConsist",
        base_numeric_id=22960,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="ExpressIntermodalCar", chassis="2_axle_1cc_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="ExpressIntermodalCarConsist",
        base_numeric_id=22970,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="ExpressIntermodalCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_type_factory)

    return result
