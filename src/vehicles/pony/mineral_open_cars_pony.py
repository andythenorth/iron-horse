from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18690,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18710,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18730,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18750,
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
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18770,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18790,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18810,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18830,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18850,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18870,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralConsist",
        base_numeric_id=18890,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    return result
