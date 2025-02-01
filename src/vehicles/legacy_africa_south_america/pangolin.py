from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(**kwargs):
    consist = EngineConsist(
        id="pangolin",
        base_numeric_id=11100,
        name="2-6-0 Pangolin",
        power=1200,
        base_track_type_name="NG",
        intro_year=1860,
    )

    consist.add_unit(type=SteamEngineUnit, weight=40, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=27, vehicle_length=4, spriterow_num=1
    )

    return consist
