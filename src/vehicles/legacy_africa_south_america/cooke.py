# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="cooke",
        base_numeric_id=9190,
        name="4-6-0 Cooke",
        power=1500,
        intro_year=1885,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=75, vehicle_length=6, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=5, rel_spriterow_index=1
    )

    return model_def
