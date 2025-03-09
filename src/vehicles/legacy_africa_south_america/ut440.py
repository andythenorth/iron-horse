# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="ut440",
        base_numeric_id=9480,
        name="UT440",
        power=900,
        intro_year=2011,
    )

    model_def.add_unit(
        type=ElectricEngineUnit, weight=40, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=ElectricEngineUnit, weight=40, vehicle_length=8, rel_spriterow_index=1
    )

    return model_def
