from train import KaolinHopperCarConsist, FreightCar


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = KaolinHopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26230,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="2_axle_filled_greebled_24px")

    result.append(consist_factory)

    consist_factory = KaolinHopperCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26240,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="4_axle_filled_greebled_32px")

    result.append(consist_factory)

    return result
