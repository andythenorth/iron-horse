from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="MailHSTCar",
        base_numeric_id=16880,
        gen=4,
        subtype="U",
        intro_year_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="MailHSTCar",
        base_numeric_id=26180,
        gen=5,
        subtype="U",
        intro_year_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="ExpressMailCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    return result
