from train import PassengerHighSpeedCarConsist, PaxCar


def main(roster_id, **kwargs):
    result = []

    consist_factory = PassengerHighSpeedCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30680,
        gen=5,
        subtype="U",
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist_factory.add_unit(type=PaxCar, chassis="high_speed_32px")

    result.append(consist_factory)

    return result
