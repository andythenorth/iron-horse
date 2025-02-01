from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(**kwargs):
    consist = EngineConsist(
        id="potosi",
        base_numeric_id=9410,
        name="4-8-2+2-8-4 Potosi",
        power=4500,
        intro_year=1935,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=5, spriterow_num=0
    )

    consist.add_unit(type=SteamEngineUnit, weight=80, vehicle_length=8, spriterow_num=1)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=5, spriterow_num=2
    )

    return consist
