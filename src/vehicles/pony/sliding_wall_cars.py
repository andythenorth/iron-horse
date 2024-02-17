from train import BoxCarSlidingWallConsist, FreightCar


def main():

    # --------------- pony NG ----------------------------------------------------------------------

    consist = BoxCarSlidingWallConsist(
        roster_id="pony",
        base_numeric_id=11540,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = BoxCarSlidingWallConsist(
        roster_id="pony",
        base_numeric_id=12340,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_24px")

    # --------------- pony ----------------------------------------------------------------------

    # starts gen 4, B and C only

    consist = BoxCarSlidingWallConsist(
        roster_id="pony",
        base_numeric_id=10610,
        gen=4,
        subtype="B",
        intro_year_offset=5,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_1cc_filled_24px")

    consist = BoxCarSlidingWallConsist(
        roster_id="pony",
        base_numeric_id=10830,
        gen=4,
        subtype="C",
        intro_year_offset=5,  # let's be a little bit later for this one
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarSlidingWallConsist(
        roster_id="pony",
        base_numeric_id=9450,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    consist = BoxCarSlidingWallConsist(
        roster_id="pony",
        base_numeric_id=9480,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarSlidingWallConsist(
        roster_id="pony",
        base_numeric_id=5190,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=4,
    )

    # --------------- ibex ----------------------------------------------------------------------

    # starts gen 5, may add gen 4 later

    consist = BoxCarSlidingWallConsist(
        roster_id="ibex",
        base_numeric_id=8730,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    consist = BoxCarSlidingWallConsist(
        roster_id="ibex",
        base_numeric_id=8740,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarSlidingWallConsist(
        roster_id="ibex",
        base_numeric_id=10,
        gen=5,
        subtype="D",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=4,
    )

    consist = BoxCarSlidingWallConsist(
        roster_id="ibex",
        base_numeric_id=8760,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    consist = BoxCarSlidingWallConsist(
        roster_id="ibex",
        base_numeric_id=8770,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )

    consist = BoxCarSlidingWallConsist(
        roster_id="ibex",
        base_numeric_id=5170,
        gen=6,
        subtype="D",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=0,
    )

    consist.add_unit(
        type=FreightCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_20px",
        symmetry_type="asymmetric",
        spriterow_num=4,
    )
