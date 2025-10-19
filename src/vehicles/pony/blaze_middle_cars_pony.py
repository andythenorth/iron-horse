from train.producer import ModelDef

# HST middle parts are not engines, unlike TGV middle parts


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="PassengerHSTMiddleCar",
        model_id="blaze_middle_passenger",
        cab_id="blaze_cab",
        base_numeric_id=18150,
        gen=5,
        subtype="U",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailHSTMiddleCar",
        model_id="blaze_middle_mail",
        cab_id="blaze_cab",
        base_numeric_id=26180,
        gen=5,
        subtype="U",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    return result
