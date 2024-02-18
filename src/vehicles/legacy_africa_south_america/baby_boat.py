from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="baby_boat",
        base_numeric_id=10630,
        name="Baby Boat",
        power=1800,
        intro_year=1978,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=120, vehicle_length=8, spriterow_num=0
    )

    return consist
