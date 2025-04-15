# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="kessler",
        base_numeric_id=11030,
        name="0-4-2 Kessler",
        power=450,
        base_track_type="NG",
        random_reverse=True,
        intro_year=1860,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=25, vehicle_length=5, rel_spriterow_index=0
    )

    return model_def
