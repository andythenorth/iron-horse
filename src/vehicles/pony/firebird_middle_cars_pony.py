from train.factory import ModelDef

# HST middle parts are not engines, unlike TGV middle parts


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="PassengerHSTMiddleCar",
        model_id="firebird_middle_passenger",
        cab_id="firebird_cab",
        base_numeric_id=18170,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailHSTMiddleCar",
        model_id="firebird_middle_mail",
        cab_id="firebird_cab",
        base_numeric_id=16880,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    return result
