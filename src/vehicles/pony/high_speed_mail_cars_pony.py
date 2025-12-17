from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="MailHighSpeedCar",
        base_numeric_id=30690,
        gen=5,
        subtype="U",
        livery_group_name="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="ExpressMailCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    return result
