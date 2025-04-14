# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="oribi",
        base_numeric_id=11020,
        name="Oribi",
        power=450,
        power_by_power_source={
            "DIESEL": 450,
        },
        base_track_type_name="NG",
        intro_year=1960,
    )

    model_def.add_unit(
        type=DieselEngineUnit,
        weight=65,
        vehicle_length=8,
        capacity=30,
        rel_spriterow_index=0,
    )

    return model_def
