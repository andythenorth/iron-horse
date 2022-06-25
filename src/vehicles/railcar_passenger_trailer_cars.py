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
        intro_date_offset=-5,  # introduce early by design
        sprites_complete=True,
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
        intro_date_offset=-5,  # introduce early by design
        sprites_complete=True,
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
        intro_date_offset=-5,  # introduce early by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_2",
    )
