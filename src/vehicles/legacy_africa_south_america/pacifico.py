from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(**kwargs):
    consist = EngineConsist(
        id="pacifico",
        base_numeric_id=9350,
        name="4-6-2 Pacifico",
        power=1800,
        intro_year=1910,
    )

    consist.add_unit(type=SteamEngineUnit, weight=90, vehicle_length=7, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=5, spriterow_num=1
    )

    return consist
