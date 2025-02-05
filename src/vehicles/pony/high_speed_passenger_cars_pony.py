from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="PassengerHighSpeedCarConsist",
        base_numeric_id=30680,
        gen=5,
        subtype="U",
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_type_factory.define_unit(class_name="PaxCar", chassis="high_speed_32px")

    result.append(model_type_factory)

    return result
