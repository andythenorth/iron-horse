# from train import foo


def main(**kwargs):  # for rest of stats, look up Chinese CKD8G
    model_def = ModelDefFoo(
        id="roca", base_numeric_id=9440, name="Roca", power=3000, intro_year=1990
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=30, vehicle_length=8, rel_spriterow_index=0
    )

    return model_def
