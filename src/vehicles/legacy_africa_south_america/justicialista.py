from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="justicialista",
        base_numeric_id=9290,
        name="Justicialista",
        power=5880,  # yes, really, it's high powered
        intro_year=1955,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=114, vehicle_length=8, spriterow_num=0
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=114, vehicle_length=8, spriterow_num=1
    )

    return consist
