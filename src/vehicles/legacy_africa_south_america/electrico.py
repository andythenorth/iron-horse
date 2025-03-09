# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="electrico",
        base_numeric_id=9220,
        name="Electrico 2-B+B-2",
        power=2400,
        intro_year=1920,
    )

    model_def.add_unit(
        type=ElectricEngineUnit, weight=140, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
