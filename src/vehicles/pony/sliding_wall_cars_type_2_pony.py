from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType2",
        base_numeric_id=20920,
        gen=3,
        intro_year_offset=15,  # let's be a little bit later for this one
        subtype="A",
        base_track_type="NG",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_ng_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType2",
        base_numeric_id=31430,
        gen=3,
        intro_year_offset=15,  # let's be a little bit later for this one
        subtype="B",
        base_track_type="NG",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_ng_24px",
    )

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------
    # starts gen 4, B and C only

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType2",
        base_numeric_id=18300,
        gen=4,
        subtype="B",
        intro_year_offset=5,  # let's be a little bit later for this one
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType2",
        base_numeric_id=23380,
        gen=4,
        subtype="C",
        intro_year_offset=5,  # let's be a little bit later for this one
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType2",
        base_numeric_id=18320,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType2",
        base_numeric_id=23220,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_greebled_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="BoxCarSlidingWallType2",
        base_numeric_id=2140,
        gen=5,
        subtype="D",
        sprites_complete=False,
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
