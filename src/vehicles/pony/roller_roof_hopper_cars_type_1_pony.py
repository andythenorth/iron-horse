from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge -----------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRollerRoofConsistType1",
        base_numeric_id=23670,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRollerRoofConsistType1",
        base_numeric_id=16840,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_24px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRollerRoofConsistType1",
        base_numeric_id=23730,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_type_factory)

    model_type_factory = ModelTypeFactory(
        class_name="MineralCoveredHopperCarRollerRoofConsistType1",
        base_numeric_id=17160,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_type_factory)

    return result
