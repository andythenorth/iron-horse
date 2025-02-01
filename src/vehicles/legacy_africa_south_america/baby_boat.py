from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist = EngineConsist(
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
