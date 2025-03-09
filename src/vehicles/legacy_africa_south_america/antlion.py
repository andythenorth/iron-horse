# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="antlion",
        base_numeric_id=10590,
        name="Antlion",
        power_by_power_source={
            "DIESEL": 350,
        },
        intro_year=1950,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=75, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
