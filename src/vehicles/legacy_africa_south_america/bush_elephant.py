# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="bush_elephant",
        base_numeric_id=11040,
        name="2-6-6-2 Bush Elephant",
        power=2200,
        base_track_type="NG",
        intro_year=1915,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=128, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=52, vehicle_length=4, rel_spriterow_index=1
    )

    return model_def
