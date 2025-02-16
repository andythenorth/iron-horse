# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="anaconda",
        base_numeric_id=9070,
        name="Anaconda",
        power_by_power_source={
            "DIESEL": 300,
        },
        intro_year=1980,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=65, vehicle_length=8, capacity=55, spriterow_num=0
    )

    return consist_cabbage
