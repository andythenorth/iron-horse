from train.train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=37020,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=37030,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=37040,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------
    # only type A for gen 1

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=23000,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_def)

    # no new type A for gen 2, gen 1 type A continues

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=23010,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="3_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=23020,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=23030,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=23040,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=23050,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=31060,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCar", chassis="4_axle_filled_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=26880,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="2_axle_filled_greebled_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarMillConsist",
        base_numeric_id=23080,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
