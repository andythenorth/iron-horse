# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="milne",
        base_numeric_id=11090,
        name="4-8-2 Milne",
        power=600,
        base_track_type_name="NG",
        random_reverse=True,
        intro_year=1910,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=50, vehicle_length=7, rel_spriterow_index=0
    )

    return model_def
