from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="springburn",
        base_numeric_id=10830,
        name="Springburn",
        power=1200,
        intro_year=1950,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=80, vehicle_length=6, spriterow_num=0
    )

    return consist
