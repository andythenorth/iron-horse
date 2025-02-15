#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="smokey_mountain",
        base_numeric_id=10650,
        name="Smokey Mountain",
        power=3200,
        intro_year=1950,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=112, vehicle_length=8, spriterow_num=0
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=112, vehicle_length=8, spriterow_num=1
    )

    return consist_cabbage
