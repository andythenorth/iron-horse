from train import EngineConsist, DieselEngineUnit


def main(roster_id):  # GE Shovelnose - meter gauge ish
    consist = EngineConsist(
        id="cooper",
        base_numeric_id=10480,
        name="Cooper",
        power_by_power_source={
            "DIESEL": 1000,
        },
        base_track_type_name="NG",
        intro_year=1949,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=85, vehicle_length=7, spriterow_num=0
    )

    return consist
