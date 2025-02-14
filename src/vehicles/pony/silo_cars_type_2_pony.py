from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="SiloCarConsistType2",
        base_numeric_id=17600,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType2",
        base_numeric_id=17620,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType2",
        base_numeric_id=30550,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType2",
        base_numeric_id=17660,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType2",
        base_numeric_id=17640,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="4_axle_filled_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="SiloCarConsistType2",
        base_numeric_id=36560,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
