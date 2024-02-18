from train import ReeferCarAltConsist, ExpressCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = ReeferCarAltConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
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
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
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
