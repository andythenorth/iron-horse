from train import MailHighSpeedCarConsist, ExpressMailCar


def main():

    consist = MailHighSpeedCarConsist(
        roster_id="pony",
        base_numeric_id=10990,
        gen=5,
        subtype="U",
        sprites_complete=False,
    )

    consist.add_unit(type=ExpressMailCar, chassis="4_axle_solid_express_32px")
