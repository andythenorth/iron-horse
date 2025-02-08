from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarMineralLowSideConsist",
        base_numeric_id=31510,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    # gen 1 also covers gen 2

    model_def = ModelDef(
        class_name="BulkOpenCarMineralLowSideConsist",
        base_numeric_id=31530,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralLowSideConsist",
        base_numeric_id=31550,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralLowSideConsist",
        base_numeric_id=31570,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralLowSideConsist",
        base_numeric_id=31590,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralLowSideConsist",
        base_numeric_id=31410,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralLowSideConsist",
        base_numeric_id=31470,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralLowSideConsist",
        base_numeric_id=31490,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    return result
