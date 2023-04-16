from train import PassengerExpressRailcarTrailerCarConsist, PaxRailcarTrailerCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = PassengerExpressRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=13720,
        gen=3,
        subtype="U",
        cab_id="high_flyer",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    consist = PassengerExpressRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=13580,
        gen=4,
        subtype="U",
        cab_id="sunshine_coast",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    consist = PassengerExpressRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=13640,
        gen=5,
        subtype="U",
        cab_id="olympic",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    consist = PassengerExpressRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=13650,
        gen=6,
        subtype="U",
        cab_id="bright_country",
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )
