from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(**kwargs):
    consist = EngineConsist(
        id="hyena",
        base_numeric_id=11120,
        name="4-6-2 Hyena",
        power=1400,
        tractive_effort_coefficient=0.19,
        base_track_type_name="NG",
        intro_year=1915,
    )

    consist.add_unit(type=SteamEngineUnit, weight=68, vehicle_length=7, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=37, vehicle_length=5, spriterow_num=1
    )

    return consist
