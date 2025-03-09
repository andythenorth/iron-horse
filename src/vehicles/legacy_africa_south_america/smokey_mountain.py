# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="smokey_mountain",
        base_numeric_id=10650,
        name="Smokey Mountain",
        power=3200,
        intro_year=1950,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=112, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=112, vehicle_length=8, rel_spriterow_index=1
    )

    return model_def
