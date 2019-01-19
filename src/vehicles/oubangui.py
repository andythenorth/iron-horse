from train import EngineConsist, SteamEngineUnit


def main():
    consist = EngineConsist(id='oubangui',
                            base_numeric_id=2010,
                            name='2-6-6-2 Oubangui',
                            power=1500,
                            base_track_type='NG',
                            intro_date=1920)

    consist.add_unit(type=SteamEngineUnit,
                     weight=90,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
