from train import PassengerHSTCarConsist, PaxCar


def main():
    # --------------- standard gauge ---------------------------------------------------------------

    consist = PassengerHSTCarConsist(
        roster_id="pony",
        base_numeric_id=12940,
        gen=4,
        subtype="U",
        intro_year_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="high_speed_32px")

    consist = PassengerHSTCarConsist(
        roster_id="pony",
        base_numeric_id=12520,
        gen=5,
        subtype="U",
        intro_year_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="high_speed_32px")
