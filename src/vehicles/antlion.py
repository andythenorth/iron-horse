from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="antlion",
        base_numeric_id=10590,
        name="Antlion",
        power_by_power_source={
            "DIESEL": 350,
        },
        intro_year=1950,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=75, vehicle_length=8, spriterow_num=0
    )

    return consist
