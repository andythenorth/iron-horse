# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="justicialista",
        base_numeric_id=9290,
        name="Justicialista",
        power=5880,  # yes, really, it's high powered
        intro_year=1955,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=114, vehicle_length=8, rel_spriterow_index=0
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=114, vehicle_length=8, rel_spriterow_index=1
    )

    return consist_cabbage
