# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="hyena",
        base_numeric_id=11120,
        name="4-6-2 Hyena",
        power=1400,
        tractive_effort_coefficient=0.19,
        base_track_type_name="NG",
        intro_year=1915,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=68, vehicle_length=7, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=37, vehicle_length=5, rel_spriterow_index=1
    )

    return model_def
