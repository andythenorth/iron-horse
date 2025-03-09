# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="patagonia",
        base_numeric_id=9370,
        name="Patagonia",
        base_track_type_name="NG",
        power=500,
        intro_year=1960,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=20, vehicle_length=7, capacity=35, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=20, vehicle_length=7, capacity=35, rel_spriterow_index=1
    )

    return model_def
