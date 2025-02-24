# from train import foo


def main(**kwargs):  # roughly an SAR 91-000 class
    consist_cabbage = ModelDefFoo(
        id="bigfoot",
        base_numeric_id=10660,
        name="Bigfoot",
        power=900,
        base_track_type_name="NG",
        intro_year=1970,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=50, vehicle_length=5, rel_spriterow_index=0
    )

    return consist_cabbage
