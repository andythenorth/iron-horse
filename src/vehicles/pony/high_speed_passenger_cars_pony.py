from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerHighSpeedCarConsist",
        base_numeric_id=30680,
        gen=5,
        subtype="U",
        livery_group_name="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="high_speed_32px")

    result.append(model_def)

    return result
