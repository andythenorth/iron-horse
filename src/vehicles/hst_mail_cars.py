from train import MailHSTCarConsist, ExpressMailCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    consist = MailHSTCarConsist(
        roster_id="pony",
        base_numeric_id=7130,
        gen=4,
        subtype="U",
        intro_date_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    consist = MailHSTCarConsist(
        roster_id="pony",
        base_numeric_id=7140,
        gen=5,
        subtype="U",
        intro_date_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")

    consist = MailHSTCarConsist(
        roster_id="pony",
        base_numeric_id=7150,
        gen=6,
        subtype="U",
        intro_date_offset=-10,  # match to Scorcher HST
        cab_id="scorcher",
        high_speed_rail_capable=True, # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")
