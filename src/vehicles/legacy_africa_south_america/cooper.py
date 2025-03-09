# from train import foo


def main(**kwargs):  # GE Shovelnose - meter gauge ish
    model_def = ModelDefFoo(
        id="cooper",
        base_numeric_id=10480,
        name="Cooper",
        power_by_power_source={
            "DIESEL": 1000,
        },
        base_track_type_name="NG",
        intro_year=1949,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=85, vehicle_length=7, rel_spriterow_index=0
    )

    return model_def
