from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="ut440",
        base_numeric_id=440,
        name="UT440",
        power=900,
        intro_date=2011,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=40, vehicle_length=8, spriterow_num=0
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=40, vehicle_length=8, spriterow_num=1
    )

    return consist
