from train.train import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="ReeferCarConsistType2",
        base_numeric_id=34790,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ReeferCarConsistType2",
        base_numeric_id=31880,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ReeferCarConsistType2",
        base_numeric_id=31890,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="3_axle_solid_express_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ReeferCarConsistType2",
        base_numeric_id=36940,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ReeferCarConsistType2",
        base_numeric_id=28110,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ReeferCarConsistType2",
        base_numeric_id=31320,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ReeferCarConsistType2",
        base_numeric_id=32610,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="ReeferCarConsistType2",
        base_numeric_id=32620,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ExpressCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(model_def)

    return result
