# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="hippo",
        base_numeric_id=10910,
        name="Hippo",
        power=3600,
        base_track_type="NG",
        intro_year=1975,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=130, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
