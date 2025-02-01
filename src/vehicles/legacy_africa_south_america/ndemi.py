from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(**kwargs):
    consist = EngineConsist(
        id="ndemi",
        base_numeric_id=11110,
        name="4-8-0 Ndemi",
        power=1700,
        base_track_type_name="NG",
        intro_year=1887,
    )

    consist.add_unit(type=SteamEngineUnit, weight=75, vehicle_length=8, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=35, vehicle_length=4, spriterow_num=1
    )

    return consist
