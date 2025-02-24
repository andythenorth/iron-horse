# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="electrico",
        base_numeric_id=9220,
        name="Electrico 2-B+B-2",
        power=2400,
        intro_year=1920,
    )

    consist_cabbage.add_unit(
        type=ElectricEngineUnit, weight=140, vehicle_length=8, rel_spriterow_index=0
    )

    return consist_cabbage
