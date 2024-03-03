from train import PassengerExpressRailcarTrailerCarConsist, PaxRailcarTrailerCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = PassengerExpressRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=6750,
        gen=3,
        subtype="U",
        cab_id="high_flyer",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    consist = PassengerExpressRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=6770,
        gen=4,
        subtype="U",
        cab_id="sunshine_coast",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    consist = PassengerExpressRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30,
        gen=5,
        subtype="U",
        cab_id="olympic",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    consist = PassengerExpressRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=6380,
        gen=6,
        subtype="U",
        cab_id="nimbus",
        lgv_capable=True,
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="high_speed_32px",
        tail_light="railcar_32px_5",
        suppress_roof_sprite=True,
        repeat=2,
    )
