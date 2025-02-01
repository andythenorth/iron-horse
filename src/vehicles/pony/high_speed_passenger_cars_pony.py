from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerHighSpeedCarConsist",
        base_numeric_id=30680,
        gen=5,
        subtype="U",
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="PaxCar", chassis="high_speed_32px")

    result.append(consist_factory)

    return result
