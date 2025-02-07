from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeConsistType2",
        base_numeric_id=24900,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeConsistType2",
        base_numeric_id=24910,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeConsistType2",
        base_numeric_id=24920,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_chute_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeConsistType2",
        base_numeric_id=24930,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_chute_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="MineralCoveredHopperCarLimeConsistType2",
        base_numeric_id=22250,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_chute_greebled_alt_32px"
    )

    result.append(model_def)

    return result
