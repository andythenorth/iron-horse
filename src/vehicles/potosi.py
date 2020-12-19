from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="potosi",
        base_numeric_id=370,
        name="4-8-2+2-8-4 Potosi",
        power=4500,
        intro_date=1935,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=5, spriterow_num=0
    )

    consist.add_unit(type=SteamEngineUnit, weight=80, vehicle_length=8, spriterow_num=1)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=5, spriterow_num=2
    )

    return consist
