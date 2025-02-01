from train import EngineConsist, SteamEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="pequeno",
        base_numeric_id=9390,
        name="0-4-0 Pequeno",
        power=350,
        base_track_type_name="NG",
        intro_year=1865,
    )

    consist.add_unit(type=SteamEngineUnit, weight=40, vehicle_length=4, spriterow_num=0)

    return consist
