# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="ge289a",
        base_numeric_id=10500,
        name="GE 289a Boxcab",
        power=1200,
        base_track_type="NG",
        intro_year=1922,
    )

    model_def.add_unit(
        type=ElectricEngineUnit, weight=64, vehicle_length=6, rel_spriterow_index=0
    )

    return model_def
