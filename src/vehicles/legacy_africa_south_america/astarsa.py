# from train import foo


def main(**kwargs):  # for rest of stats, look up EMD G22CW
    model_def = ModelDefFoo(
        id="astarsa", base_numeric_id=9090, name="Astarsa", power=1600, intro_year=1969
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=40, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
