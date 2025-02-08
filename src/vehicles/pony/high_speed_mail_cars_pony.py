from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailHighSpeedCarConsist",
        base_numeric_id=30690,
        gen=5,
        subtype="U",
        liveries="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit(class_name="ExpressMailCar", chassis="high_speed_32px")

    result.append(model_def)

    return result
