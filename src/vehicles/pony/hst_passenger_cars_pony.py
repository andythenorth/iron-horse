from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="PassengerHSTCarConsist",
        base_numeric_id=30330,
        gen=4,
        subtype="U",
        intro_year_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="PaxCar", chassis="high_speed_32px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="PassengerHSTCarConsist",
        base_numeric_id=30340,
        gen=5,
        subtype="U",
        intro_year_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    model_def.define_unit(class_name="PaxCar", chassis="high_speed_32px")

    result.append(model_def)

    return result
