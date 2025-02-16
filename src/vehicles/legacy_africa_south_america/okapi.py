# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="okapi",
        base_numeric_id=11000,
        name="Okapi",
        power=1850,
        base_track_type_name="NG",
        intro_year=1958,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=100, vehicle_length=7, spriterow_num=0
    )

    return consist_cabbage
