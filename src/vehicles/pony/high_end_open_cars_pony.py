from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="OpenCarHighEndConsist",
        base_numeric_id=23590,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarHighEndConsist",
        base_numeric_id=23600,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarHighEndConsist",
        base_numeric_id=23610,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="OpenCarHighEndConsist",
        base_numeric_id=23620,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarHighEndConsist",
        base_numeric_id=23630,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarHighEndConsist",
        base_numeric_id=23640,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_filled_greebled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarHighEndConsist",
        base_numeric_id=23650,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_filled_greebled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="OpenCarHighEndConsist",
        base_numeric_id=23660,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_filled_greebled_32px")

    result.append(model_def)

    return result
