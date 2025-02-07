from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="SiloCarConsistType1",
        base_numeric_id=32720,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="SiloCarConsistType1",
        base_numeric_id=17390,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="SiloCarConsistType1",
        base_numeric_id=17430,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="SiloCarConsistType1",
        base_numeric_id=32660,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="SiloCarConsistType1",
        base_numeric_id=17410,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hopppers_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="SiloCarConsistType1",
        base_numeric_id=32680,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_hoppers_32px"
    )

    result.append(model_def)

    return result
