from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="hippo",
        base_numeric_id=10910,
        name="Hippo",
        power=3600,
        base_track_type_name="NG",
        intro_year=1975,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=130, vehicle_length=8, spriterow_num=0
    )

    return consist
