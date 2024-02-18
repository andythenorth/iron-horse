from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="baldwin",
        base_numeric_id=9100,
        name="2-8-2 Baldwin",
        power=1600,
        base_track_type_name="NG",
        intro_year=1920,
    )

    consist.add_unit(type=SteamEngineUnit, weight=70, vehicle_length=7, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=25, vehicle_length=4, spriterow_num=1
    )

    return consist
