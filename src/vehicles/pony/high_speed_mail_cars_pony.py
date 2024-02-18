from train import MailHighSpeedCarConsist, ExpressMailCar


def main(roster_id, **kwargs):
    consist = MailHighSpeedCarConsist(
        roster_id=roster_id,
        roster_id_providing_module = kwargs["roster_id_providing_module"],
        base_numeric_id=10990,
        gen=5,
        subtype="U",
        liveries="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="high_speed_32px")
