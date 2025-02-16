# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="estados",
        base_numeric_id=9230,
        name="Estados Boxcab",
        power=1450,
        intro_year=1925,
    )

    consist_cabbage.add_unit(
        type=ElectricEngineUnit, weight=90, vehicle_length=6, spriterow_num=0
    )

    return consist_cabbage
