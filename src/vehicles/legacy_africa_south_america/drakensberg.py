# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="drakensberg",
        # !! This vehicle needs more than one id range due to length
        base_numeric_id=10840,
        name="4-8-2+2-8-4 Drakensberg",
        tractive_effort_coefficient=0.25,
        power=3000,
        base_track_type="NG",
        intro_year=1945,
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=4, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=80, vehicle_length=6, rel_spriterow_index=1
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=4, rel_spriterow_index=2
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=45, vehicle_length=6, rel_spriterow_index=3
    )

    return model_def
