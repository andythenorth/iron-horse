from train.factory import ModelDef

# note that the graphics files for HSTs *are* named foo_middle_mail.png etc
# for the model def, it's not worth trying to follow the TGV pattern where foo_cab.py is followed by foo_middle_mail.py
# TGV middle parts are engines, HST middle parts are currently not, it's TMWFTLB to change
# !! the simple thing would just be to name a module per HST middle part?

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
        intro_year_offset=0,  # match to Firebird # CABBAGE GET THIS FROM cab
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerHSTMiddleCar",
        model_id="blaze_middle_passenger",
        cab_id="blaze_cab",
        base_numeric_id=18150,
        gen=5,
        subtype="U",
        intro_year_offset=-10,  # match to Blaze HST # CABBAGE GET THIS FROM cab
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="high_speed_32px")

    result.append(model_def)

    return result
