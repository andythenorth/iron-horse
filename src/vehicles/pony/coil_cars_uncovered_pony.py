from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # start gen 4

    model_def = ModelDef(
        class_name="CoilCarUncoveredConsist",
        base_numeric_id=24040,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarUncoveredConsist",
        base_numeric_id=24050,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarUncoveredConsist",
        base_numeric_id=24060,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_gapped_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarUncoveredConsist",
        base_numeric_id=24070,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="CoilCarUncoveredConsist",
        base_numeric_id=24080,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    return result
