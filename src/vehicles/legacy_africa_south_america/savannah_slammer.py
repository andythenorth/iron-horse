# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="savannah_slammer",
        base_numeric_id=10580,
        name="Savannah Slammer",
        power=500,
        intro_year=1980,
    )

    model_def.add_unit(
        type=DieselEngineUnit,
        weight=65,
        vehicle_length=8,
        capacity=65,
        rel_spriterow_index=0,
    )

    return model_def
