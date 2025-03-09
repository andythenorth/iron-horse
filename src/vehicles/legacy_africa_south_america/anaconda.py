# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="anaconda",
        base_numeric_id=9070,
        name="Anaconda",
        power_by_power_source={
            "DIESEL": 300,
        },
        intro_year=1980,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=65, vehicle_length=8, capacity=55, rel_spriterow_index=0
    )

    return model_def
