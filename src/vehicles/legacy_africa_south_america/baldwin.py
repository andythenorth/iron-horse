# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="baldwin",
        base_numeric_id=9100,
        name="2-8-2 Baldwin",
        power=1600,
        base_track_type="NG",
        intro_year=1920,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=70, vehicle_length=7, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=25, vehicle_length=4, rel_spriterow_index=1
    )

    return model_def
