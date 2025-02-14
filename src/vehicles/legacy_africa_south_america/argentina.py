from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(**kwargs):
    consist_cabbage = EngineConsist(
        id="argentina",
        base_numeric_id=9080,
        name="4-8-0 Argentina",
        power=1800,
        intro_year=1910,
    )

    consist_cabbage.add_unit(
        type=SteamEngineUnit, weight=100, vehicle_length=8, spriterow_num=0
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=5, spriterow_num=1
    )

    return consist_cabbage
