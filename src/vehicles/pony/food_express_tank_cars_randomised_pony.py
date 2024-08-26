from train import ExpressFoodTankCarRandomisedConsist, FreightCar


def main(roster_id, **kwargs):

    # --------------- standard gauge ---------------------------------------------------------------


    consist = ExpressFoodTankCarRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28160,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = ExpressFoodTankCarRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=28170,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
