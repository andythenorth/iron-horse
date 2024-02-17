from train import ReeferCarConsist, ExpressCar


def main():
    # --------------- standard gauge ---------------------------------------------------------------    # no gen 1 reefer - straight to gen 2

    consist = ReeferCarConsist(
        roster_id="ibex",
        base_numeric_id=8470,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    consist = ReeferCarConsist(
        roster_id="ibex",
        base_numeric_id=8480,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    consist = ReeferCarConsist(
        roster_id="ibex",
        base_numeric_id=8490,
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
        roster_id="ibex",
        base_numeric_id=8620,
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
        roster_id="ibex",
        base_numeric_id=8630,
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
        roster_id="ibex",
        base_numeric_id=8640,
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
        roster_id="ibex",
        base_numeric_id=8650,
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
        roster_id="ibex",
        base_numeric_id=8660,
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
        roster_id="ibex",
        base_numeric_id=8670,
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
        roster_id="ibex",
        base_numeric_id=8680,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )
