from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(**kwargs):
    consist_cabbage = EngineConsist(
        id="cooke",
        base_numeric_id=9190,
        name="4-6-0 Cooke",
        power=1500,
        intro_year=1885,
    )

    consist_cabbage.add_unit(type=SteamEngineUnit, weight=75, vehicle_length=6, spriterow_num=0)

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=5, spriterow_num=1
    )

    return consist_cabbage
