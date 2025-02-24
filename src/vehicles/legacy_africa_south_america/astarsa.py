# from train import foo


def main(**kwargs):  # for rest of stats, look up EMD G22CW
    consist_cabbage = ModelDefFoo(
        id="astarsa", base_numeric_id=9090, name="Astarsa", power=1600, intro_year=1969
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=40, vehicle_length=8, rel_spriterow_index=0
    )

    return consist_cabbage
