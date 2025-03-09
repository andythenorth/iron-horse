# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="hofman",
        base_numeric_id=10880,
        name="2-6-2+2-6-2 Hofman",
        tractive_effort_coefficient=0.27,  # dibble for game balance
        power=750,
        base_track_type_name="NG",
        intro_year=1940,
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=15, vehicle_length=3, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=30, vehicle_length=4, rel_spriterow_index=1
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=15, vehicle_length=3, rel_spriterow_index=2
    )

    return model_def
