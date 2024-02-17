from train import EngineConsist, DieselEngineUnit


def main(roster_id):  # for rest of stats, look up GE Export models U5B-U8B
    consist = EngineConsist(
        id="universal",
        base_numeric_id=9580,
        name="Universal",
        power=800,
        power_by_power_source={
            "DIESEL": 800,
        },
        intro_year=1958,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=65, vehicle_length=7, spriterow_num=0
    )

    return consist
