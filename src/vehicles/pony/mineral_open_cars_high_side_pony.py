from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=23550,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=38560,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=23570,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=18910,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=18930,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=18950,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=18970,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=18990,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=19010,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=19030,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BulkOpenCarMineralHighSideConsist",
        base_numeric_id=19050,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="4_axle_gapped_greebled_32px"
    )

    result.append(model_def)

    return result
