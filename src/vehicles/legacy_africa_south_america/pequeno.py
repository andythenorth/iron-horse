# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="pequeno",
        base_numeric_id=9390,
        name="0-4-0 Pequeno",
        power=350,
        base_track_type="NG",
        intro_year=1865,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=40, vehicle_length=4, rel_spriterow_index=0
    )

    return model_def
