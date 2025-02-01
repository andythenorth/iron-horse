from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="planet",
        base_numeric_id=360,
        name="Planet",
        base_track_type_name="NG",
        power=500,
        intro_year=1950,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=40, vehicle_length=4, spriterow_num=0
    )

    return consist
