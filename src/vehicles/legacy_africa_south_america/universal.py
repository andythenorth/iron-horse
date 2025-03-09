# from train import foo


def main(**kwargs):  # for rest of stats, look up GE Export models U5B-U8B
    model_def = ModelDefFoo(
        id="universal",
        base_numeric_id=9580,
        name="Universal",
        power=800,
        power_by_power_source={
            "DIESEL": 800,
        },
        intro_year=1958,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=65, vehicle_length=7, rel_spriterow_index=0
    )

    return model_def
