# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="super_mountain",
        base_numeric_id=9550,
        name="4-8-4 Super Mountain",
        power=2100,
        intro_year=1935,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=110, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=60, vehicle_length=6, rel_spriterow_index=1
    )

    return model_def
