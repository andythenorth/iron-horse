from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # starts gen 4, B and C only

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType3",
        base_numeric_id=17020,
        gen=4,
        subtype="B",
        intro_year_offset=5,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_filled_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType3",
        base_numeric_id=27820,
        gen=4,
        subtype="C",
        intro_year_offset=5,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_greebled_alt_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType3",
        base_numeric_id=28680,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType3",
        base_numeric_id=28700,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_greebled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType3",
        base_numeric_id=6750,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_20px",
        symmetry_type="asymmetric",
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_20px",
        symmetry_type="asymmetric",
        rel_spriterow_index=4,
    )

    result.append(model_def)

    return result
