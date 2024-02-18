from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="peacock",
        base_numeric_id=9380,
        name="2-6-0 Peacock",
        power_by_power_source={
            "STEAM": 1200,
        },
        tractive_effort_coefficient=0.32,
        intro_year=1885,
    )

    consist.add_unit(type=SteamEngineUnit, weight=65, vehicle_length=6, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=45, vehicle_length=4, spriterow_num=1
    )

    return consist
