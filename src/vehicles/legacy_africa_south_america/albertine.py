# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="albertine",
        base_numeric_id=11080,
        name="4-4-2 Albertine",
        power=1200,
        tractive_effort_coefficient=0.19,
        base_track_type_name="NG",
        intro_year=1885,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=45, vehicle_length=7, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=4, rel_spriterow_index=1
    )

    return model_def
