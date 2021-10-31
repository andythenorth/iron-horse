from train import PassengerHSTCarConsist, PaxCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = PassengerHSTCarConsist(
        roster_id="pony",
        base_numeric_id=3900,
        gen=4,
        subtype="U",
        intro_date_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerHSTCarConsist(
        roster_id="pony",
        base_numeric_id=3480,
        gen=5,
        subtype="U",
        intro_date_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")

    consist = PassengerHSTCarConsist(
        roster_id="pony",
        base_numeric_id=3490,
        gen=6,
        subtype="U",
        intro_date_offset=-10,  # match to Scorcher HST
        cab_id="scorcher",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")
