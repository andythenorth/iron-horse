from train import ReeferCarConsist, ExpressCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------    # no gen 1 reefer - straight to gen 2

    consist = ReeferCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=9770,
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
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=9760,
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
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=16430,
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
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11600,
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
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11630,
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
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=12620,
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
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11610,
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
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=11620,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=ExpressCar,
        suppress_roof_sprite=True,  # non-standard roof for this wagon
        chassis="4_axle_filled_greebled_32px",
    )
