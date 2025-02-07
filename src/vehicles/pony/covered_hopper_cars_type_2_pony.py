from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="CoveredHopperCarConsistType2",
        base_numeric_id=24010,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="2_axle_chute_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="CoveredHopperCarConsistType2",
        base_numeric_id=17800,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="CoveredHopperCarConsistType2",
        base_numeric_id=23240,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="CoveredHopperCarConsistType2",
        base_numeric_id=17820,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="CoveredHopperCarConsistType2",
        base_numeric_id=37070,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_chute_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="CoveredHopperCarConsistType2",
        base_numeric_id=36320,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_chute_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="CoveredHopperCarConsistType2",
        base_numeric_id=17840,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_chute_greebled_alt_32px"
    )

    result.append(model_def)

    return result
