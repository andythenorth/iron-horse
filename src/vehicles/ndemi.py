from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='ndemi',
                            base_numeric_id=2070,
                            name='4-8-0 Ndemi',
                            power=1700,
                            base_track_type='NG',
                            intro_date=1887)

    consist.add_unit(type=SteamEngineUnit,
                     weight=75,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=35,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
