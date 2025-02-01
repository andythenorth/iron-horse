from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="okapi",
        base_numeric_id=11000,
        name="Okapi",
        power=1850,
        base_track_type_name="NG",
        intro_year=1958,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=100, vehicle_length=7, spriterow_num=0
    )

    return consist
