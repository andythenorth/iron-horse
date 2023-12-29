from train import PassengerHighSpeedCarConsist, PaxCar


def main():

    consist = PassengerHighSpeedCarConsist(
        roster_id="pony",
        base_numeric_id=11020,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="4_axle_solid_express_32px")
