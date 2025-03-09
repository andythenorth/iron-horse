# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="potosi",
        base_numeric_id=9410,
        name="4-8-2+2-8-4 Potosi",
        power=4500,
        intro_year=1935,
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=5, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=80, vehicle_length=8, rel_spriterow_index=1
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=5, rel_spriterow_index=2
    )

    return model_def
