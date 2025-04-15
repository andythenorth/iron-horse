from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType1",
        base_numeric_id=26980,
        gen=3,
        intro_year_offset=15,  # let's be a little bit later for this one
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType1",
        base_numeric_id=22080,
        gen=3,
        intro_year_offset=15,  # let's be a little bit later for this one
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------
    # starts gen 4, B and C only

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType1",
        base_numeric_id=27000,
        gen=4,
        subtype="B",
        intro_year_offset=5,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType1",
        base_numeric_id=22100,
        gen=4,
        subtype="C",
        intro_year_offset=5,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType1",
        base_numeric_id=27020,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType1",
        base_numeric_id=22120,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType1",
        base_numeric_id=5190,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        rel_spriterow_index=4,
    )

    result.append(model_def)

    return result
