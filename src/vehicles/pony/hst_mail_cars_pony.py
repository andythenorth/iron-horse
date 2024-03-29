from train import MailHSTCarConsist, ExpressMailCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = MailHSTCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=16880,
        gen=4,
        subtype="U",
        intro_year_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="high_speed_32px")

    consist = MailHSTCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=26180,
        gen=5,
        subtype="U",
        intro_year_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="high_speed_32px")
