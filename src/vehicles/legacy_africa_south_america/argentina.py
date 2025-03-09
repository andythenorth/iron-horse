# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="argentina",
        base_numeric_id=9080,
        name="4-8-0 Argentina",
        power=1800,
        intro_year=1910,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=100, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=5, rel_spriterow_index=1
    )

    return model_def
