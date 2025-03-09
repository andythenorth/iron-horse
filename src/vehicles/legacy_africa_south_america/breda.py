# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="breda",
        base_numeric_id=9120,
        name="Breda E32",
        power=900,
        intro_year=1961,
    )

    model_def.add_unit(
        type=ElectricEngineUnit, weight=40, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
