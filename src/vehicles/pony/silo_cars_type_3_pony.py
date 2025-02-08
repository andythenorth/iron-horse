from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="SiloCarConsistType3",
        base_numeric_id=27990,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType3",
        base_numeric_id=28010,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType3",
        base_numeric_id=28030,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType3",
        base_numeric_id=28050,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType3",
        base_numeric_id=28070,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType3",
        base_numeric_id=28090,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
