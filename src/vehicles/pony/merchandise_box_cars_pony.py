from train import BoxCarMerchandiseConsist, FreightCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = BoxCarMerchandiseConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16480,
        gen=3,
        subtype="A",
        sprites_complete=True, # needs to be improved, but eh
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarMerchandiseConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25610,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_filled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24830,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = BoxCarMerchandiseConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25630,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_24px")

    consist = BoxCarMerchandiseConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16450,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="4_axle_filled_32px",
    )

    consist = BoxCarMerchandiseConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25650,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="2_axle_filled_greebled_24px",
    )

    consist = BoxCarMerchandiseConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=24810,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=FreightCar,
        chassis="4_axle_filled_greebled_32px",
    )
