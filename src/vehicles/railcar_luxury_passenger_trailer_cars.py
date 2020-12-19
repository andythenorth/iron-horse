from train import PassengerLuxuryRailcarTrailerCarConsist, PaxLuxuryRailcarTrailerCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = PassengerLuxuryRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=4680,
        gen=3,
        subtype="U",
        intro_date_offset=2,  # introduce later by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxLuxuryRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    consist = PassengerLuxuryRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=4540,
        gen=4,
        subtype="U",
        intro_date_offset=1,  # introduce later by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxLuxuryRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    consist = PassengerLuxuryRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=4600,
        gen=5,
        subtype="U",
        intro_date_offset=1,  # introduce later by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxLuxuryRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )

    consist = PassengerLuxuryRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=4610,
        gen=6,
        subtype="U",
        intro_date_offset=1,  # introduce later by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=PaxLuxuryRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
    )
