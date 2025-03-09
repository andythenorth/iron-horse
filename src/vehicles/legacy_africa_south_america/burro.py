# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="burro",
        base_numeric_id=9130,
        name="0-4-2 Burro",
        power=650,
        intro_year=1850,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=40, vehicle_length=6, rel_spriterow_index=0
    )

    return model_def
