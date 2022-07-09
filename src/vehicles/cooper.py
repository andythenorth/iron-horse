from train import EngineConsist, DieselEngineUnit


def main():  # GE Shovelnose - meter gauge ish
    consist = EngineConsist(
        id="cooper",
        base_numeric_id=10480,
        name="Cooper",
        power=1000,
        base_track_type="NG",
        intro_year=1949,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=85, vehicle_length=7, spriterow_num=0
    )

    return consist
