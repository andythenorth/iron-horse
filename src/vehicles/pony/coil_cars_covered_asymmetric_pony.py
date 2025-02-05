from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # start gen 4

    model_type_factory = ModelTypeFactory(
        class_name="CoilCarCoveredAsymmetricConsist",
        base_numeric_id=23320,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="CoilCarAsymmetric", chassis="4_axle_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="CoilCarCoveredAsymmetricConsist",
        base_numeric_id=23330,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="CoilCarAsymmetric", chassis="4_axle_filled_32px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="CoilCarCoveredAsymmetricConsist",
        base_numeric_id=23340,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="CoilCarAsymmetric", chassis="4_axle_1cc_filled_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="CoilCarCoveredAsymmetricConsist",
        base_numeric_id=23350,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="CoilCarAsymmetric", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_type_factory)

    return result
