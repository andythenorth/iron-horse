from train import EngineConsist, ElectricEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="ut440",
        base_numeric_id=9480,
        name="UT440",
        power=900,
        intro_year=2011,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=40, vehicle_length=8, spriterow_num=0
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=40, vehicle_length=8, spriterow_num=1
    )

    return consist
