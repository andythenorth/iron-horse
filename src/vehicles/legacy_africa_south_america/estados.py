# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="estados",
        base_numeric_id=9230,
        name="Estados Boxcab",
        power=1450,
        intro_year=1925,
    )

    model_def.add_unit(
        type=ElectricEngineUnit, weight=90, vehicle_length=6, rel_spriterow_index=0
    )

    return model_def
