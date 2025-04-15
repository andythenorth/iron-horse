# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="okapi",
        base_numeric_id=11000,
        name="Okapi",
        power=1850,
        base_track_type="NG",
        intro_year=1958,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=100, vehicle_length=7, rel_spriterow_index=0
    )

    return model_def
