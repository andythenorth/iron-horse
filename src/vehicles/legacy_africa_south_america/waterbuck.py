# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="waterbuck",
        base_numeric_id=11060,
        name="Waterbuck",
        power_by_power_source={
            "DIESEL": 2200,
        },
        base_track_type_name="NG",
        intro_year=1990,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=120, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
