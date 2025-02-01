from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(**kwargs):
    consist = EngineConsist(
        id="albertine",
        base_numeric_id=11080,
        name="4-4-2 Albertine",
        power=1200,
        tractive_effort_coefficient=0.19,
        base_track_type_name="NG",
        intro_year=1885,
    )

    consist.add_unit(type=SteamEngineUnit, weight=45, vehicle_length=7, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=4, spriterow_num=1
    )

    return consist
