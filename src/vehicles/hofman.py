from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='hofman',
                            base_numeric_id=1840,
                            name='2-6-2+2-6-2 Hofman',
                            tractive_effort_coefficient=0.27,  # dibble for game balance
                            power=750,
                            base_track_type='NG',
                            intro_date=1940)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=15,
                     vehicle_length=3,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineUnit,
                     weight=30,
                     vehicle_length=4,
                     spriterow_num=1)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=15,
                     vehicle_length=3,
                     spriterow_num=2)

    return consist
