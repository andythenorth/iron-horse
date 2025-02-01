from train import BoxCarSlidingWallConsistType2


def main(roster_id, **kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    consist_factory = BoxCarSlidingWallConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23360,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(consist_factory)

    consist_factory = BoxCarSlidingWallConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=31430,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    # --------------- standard gauge ---------------------------------------------------------------
    # starts gen 4, B and C only

    consist_factory = BoxCarSlidingWallConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18300,
        gen=4,
        subtype="B",
        intro_year_offset=3,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="FreightCar", chassis="2_axle_1cc_filled_24px")

    result.append(consist_factory)

    consist_factory = BoxCarSlidingWallConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23380,
        gen=4,
        subtype="C",
        intro_year_offset=3,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(consist_factory)

    consist_factory = BoxCarSlidingWallConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=18320,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    result.append(consist_factory)

    consist_factory = BoxCarSlidingWallConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=23220,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    result.append(consist_factory)

    consist_factory = BoxCarSlidingWallConsistType2(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=6130,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    consist_factory.add_unit(
        class_name="FreightCar",
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=2,
    )

    result.append(consist_factory)

    return result
