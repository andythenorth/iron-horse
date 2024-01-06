from train import ReeferCarAltConsist, ExpressCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    # no gen 1 reefer alt - straight to gen 2

    consist = ReeferCarAltConsist(
        roster_id="pony",
        base_numeric_id=15610,
        gen=2,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=False,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    consist = ReeferCarAltConsist(
        roster_id="pony",
        base_numeric_id=15620,
        gen=3,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=False,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    consist = ReeferCarAltConsist(
        roster_id="pony",
        base_numeric_id=15630,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=False,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    consist = ReeferCarAltConsist(
        roster_id="pony",
        base_numeric_id=15640,
        gen=4,
        subtype="A",
        sprites_complete=False,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=False,  # non-standard roof for this wagon
        chassis="2_axle_filled_16px",
    )

    consist = ReeferCarAltConsist(
        roster_id="pony",
        base_numeric_id=15650,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=False,  # non-standard roof for this wagon
        chassis="2_axle_filled_24px",
    )

    consist = ReeferCarAltConsist(
        roster_id="pony",
        base_numeric_id=15660,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=False,  # non-standard roof for this wagon
        chassis="4_axle_filled_32px",
    )

    consist = ReeferCarAltConsist(
        roster_id="pony",
        base_numeric_id=10860,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="2_axle_1cc_filled_24px",
    )

    consist = ReeferCarAltConsist(
        roster_id="pony",
        base_numeric_id=10890,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_1cc_filled_32px",
    )
