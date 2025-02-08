from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    """

    model_def =ModelDef(
        class_name="BolsterCarHighEndConsist",
        base_numeric_id=30900,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)


    model_def =ModelDef(
        class_name="BolsterCarHighEndConsist",
        base_numeric_id=34540,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)
    """
    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="BolsterCarHighEndConsist",
        base_numeric_id=28120,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BolsterCarHighEndConsist",
        base_numeric_id=36580,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_gapped_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BolsterCarHighEndConsist",
        base_numeric_id=36590,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BolsterCarHighEndConsist",
        base_numeric_id=31070,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit(class_name="FreightCar", chassis="4_axle_filled_greebled_32px")

    result.append(model_def)

    return result
