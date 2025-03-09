# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="americano",
        base_numeric_id=9060,
        name="4-4-0 Americano",
        power=1000,
        intro_year=1850,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=52, vehicle_length=5, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=4, rel_spriterow_index=1
    )

    return model_def
