# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="v8",
        base_numeric_id=9450,
        name="V8 2-C+C-2",
        power=4000,
        intro_year=1949,
    )

    consist_cabbage.add_unit(
        type=ElectricEngineUnit, weight=160, vehicle_length=8, rel_spriterow_index=0
    )

    return consist_cabbage
