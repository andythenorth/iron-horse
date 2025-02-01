from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="smokey_mountain",
        base_numeric_id=10650,
        name="Smokey Mountain",
        power=3200,
        intro_year=1950,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=112, vehicle_length=8, spriterow_num=0
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=112, vehicle_length=8, spriterow_num=1
    )

    return consist
