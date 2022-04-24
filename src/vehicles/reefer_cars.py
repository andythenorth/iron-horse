from train import ReeferCarConsist, ExpressCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    # no gen 1 reefer - straight to gen 2

    consist = ReeferCarConsist(
        roster_id="pony", base_numeric_id=730, gen=2, subtype="A", sprites_complete=True
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    consist = ReeferCarConsist(
        roster_id="pony", base_numeric_id=720, gen=3, subtype="A", sprites_complete=True
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    consist = ReeferCarConsist(
        roster_id="pony",
        base_numeric_id=7390,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    consist = ReeferCarConsist(
        roster_id="pony",
        base_numeric_id=2560,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    consist = ReeferCarConsist(
        roster_id="pony",
        base_numeric_id=2590,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    consist = ReeferCarConsist(
        roster_id="pony",
        base_numeric_id=3580,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_32px",
    )

    consist = ReeferCarConsist(
        roster_id="pony",
        base_numeric_id=2570,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_greebled_24px",
    )

    consist = ReeferCarConsist(
        roster_id="pony",
        base_numeric_id=2580,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_greebled_32px",
    )

    consist = ReeferCarConsist(
        roster_id="pony",
        base_numeric_id=1820,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    consist = ReeferCarConsist(
        roster_id="pony",
        base_numeric_id=1850,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )
