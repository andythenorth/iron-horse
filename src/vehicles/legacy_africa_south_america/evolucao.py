# coding=utf-8

# from train import foo


def main(**kwargs):
    # for rest of stats, look up GE Evolution
    model_def = ModelDefFoo(
        id="evolucao",
        base_numeric_id=9240,
        name="Evolução",
        power=4400,
        intro_year=1995,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=40, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
