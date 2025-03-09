# from train import foo


def main(**kwargs):  # for rest of stats, look up Krauss Maffei Brazil
    model_def = ModelDefFoo(
        id="krauss",
        base_numeric_id=9300,
        name="Krauss",
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 3500,
        },
        intro_year=1963,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=150, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
