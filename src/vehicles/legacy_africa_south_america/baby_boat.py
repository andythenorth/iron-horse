# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="baby_boat",
        base_numeric_id=10630,
        name="Baby Boat",
        power=1800,
        intro_year=1978,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=120, vehicle_length=8, rel_spriterow_index=0
    )

    return consist_cabbage
