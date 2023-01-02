from train import (
    PassengerRailcarTrailerCarConsist,
    PaxRailcarTrailerCar,
)


def main():
    # --------------- pony NG----------------------------------------------------------------------

    # Pony NG uses railbus trailers, not railcar

    # --------------- pony ----------------------------------------------------------------------

    # gen 3 could be added but needs the engine grilles replacing with pax car pixels

    consist = PassengerRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=11980,
        gen=4,
        subtype="U",
        sprites_complete=True,
        cab_id="slammer",
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    consist = PassengerRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=14930,
        gen=4,
        subtype="U",
        sprites_complete=False,
        cab_id="geronimo",
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    consist = PassengerRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=11950,
        gen=5,
        subtype="U",
        sprites_complete=True,
        cab_id="tin_rocket",
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    consist = PassengerRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=14910,
        gen=5,
        subtype="U",
        sprites_complete=False,
        cab_id="breeze",
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    consist = PassengerRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=11090,
        gen=6,
        subtype="U",
        cab_id="happy_train",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )

    consist = PassengerRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=14920,
        gen=6,
        subtype="U",
        cab_id="zeus",
        sprites_complete=False,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )
