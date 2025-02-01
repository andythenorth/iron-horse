from train import EngineConsist, SteamEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="oubangui",
        base_numeric_id=11050,
        name="2-6-6-2 Oubangui",
        power=1500,
        base_track_type_name="NG",
        intro_year=1920,
    )

    consist.add_unit(type=SteamEngineUnit, weight=90, vehicle_length=8, spriterow_num=0)

    return consist
