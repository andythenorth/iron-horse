# from train import foo


def main(**kwargs):  # standard gauge GE Shovelnose
    model_def = ModelDefFoo(
        id="pala", base_numeric_id=9360, name="Pala", power=1200, intro_year=1955
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=105, vehicle_length=7, rel_spriterow_index=0
    )

    return model_def
