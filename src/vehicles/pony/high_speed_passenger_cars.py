from train import PassengerHighSpeedCarConsist, PaxCar


def main():
    consist = PassengerHighSpeedCarConsist(
        roster_id="pony",
        base_numeric_id=11020,
        gen=5,
        subtype="U",
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="high_speed_32px")
