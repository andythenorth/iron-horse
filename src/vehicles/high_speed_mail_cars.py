from train import MailHighSpeedCarConsist, ExpressMailCar


def main():

    consist = MailHighSpeedCarConsist(
        roster_id="pony",
        base_numeric_id=10990,
        gen=5,
        subtype="U",
        liveries="gen_5_and_6_mail_liveries", # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")
