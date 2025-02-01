from train import EngineConsist, SteamEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="burro",
        base_numeric_id=9130,
        name="0-4-2 Burro",
        power=650,
        intro_year=1850,
    )

    consist.add_unit(type=SteamEngineUnit, weight=40, vehicle_length=6, spriterow_num=0)

    return consist
