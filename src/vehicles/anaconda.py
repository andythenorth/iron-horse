from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="anaconda",
        base_numeric_id=30,
        name="Anaconda",
        power=300,
        intro_date=1980,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=65, vehicle_length=8, capacity=55, spriterow_num=0
    )

    return consist
