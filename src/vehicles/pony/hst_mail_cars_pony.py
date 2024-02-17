from train import MailHSTCarConsist, ExpressMailCar


def main():
    # --------------- standard gauge ---------------------------------------------------------------

    consist = MailHSTCarConsist(
        roster_id="pony",
        base_numeric_id=16170,
        gen=4,
        subtype="U",
        intro_year_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="high_speed_32px")

    consist = MailHSTCarConsist(
        roster_id="pony",
        base_numeric_id=16180,
        gen=5,
        subtype="U",
        intro_year_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="high_speed_32px")
