# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="pangolin",
        base_numeric_id=11100,
        name="2-6-0 Pangolin",
        power=1200,
        base_track_type="NG",
        intro_year=1860,
    )

    model_def.add_unit(
        type=SteamEnginePoweredUnit, weight=40, vehicle_length=6, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=SteamEngineTenderUnit, weight=27, vehicle_length=4, rel_spriterow_index=1
    )

    return model_def
