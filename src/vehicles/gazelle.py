from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="gazelle",
        base_numeric_id=2030,
        name="Gazelle",
        power=1800,
        base_track_type="NG",
        intro_date=1975,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=90, vehicle_length=7, spriterow_num=0
    )

    return consist
