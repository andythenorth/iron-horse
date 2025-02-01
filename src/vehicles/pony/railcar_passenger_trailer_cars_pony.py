from train import (
    PassengerRailcarTrailerCarConsist,
    PaxRailcarTrailerCar,
)


def main(roster_id, **kwargs):
    result = []

    # --------------- pony NG----------------------------------------------------------------------

    # Pony NG uses railbus trailers, not railcar

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 3 could be added but needs the engine grilles replacing with pax car pixels

    consist_factory = PassengerRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17130,
        gen=4,
        subtype="U",
        sprites_complete=True,
        cab_id="slammer",
    )

    consist_factory.add_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    result.append(consist_factory)

    consist_factory = PassengerRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26060,
        gen=4,
        subtype="U",
        sprites_complete=True,
        cab_id="geronimo",
    )

    consist_factory.add_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    result.append(consist_factory)

    consist_factory = PassengerRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=27170,
        gen=5,
        subtype="U",
        sprites_complete=True,
        cab_id="tin_rocket",
    )

    consist_factory.add_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    result.append(consist_factory)

    consist_factory = PassengerRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25140,
        gen=5,
        subtype="U",
        sprites_complete=True,
        cab_id="breeze",
    )

    consist_factory.add_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    result.append(consist_factory)

    consist_factory = PassengerRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25580,
        gen=6,
        subtype="U",
        cab_id="happy_train",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    result.append(consist_factory)

    consist_factory = PassengerRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=25400,
        gen=6,
        subtype="U",
        cab_id="zeus",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="PaxRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    result.append(consist_factory)

    return result
