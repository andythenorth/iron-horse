from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

def main():    
    consist = EngineConsist(id='pangolin',
                            base_numeric_id=2060,
                            name='2-6-0 Pangolin',
                            power=1200,
                            base_track_type='NG',
                            intro_date=1860)
    
    consist.add_unit(type=SteamEngineUnit,
                     weight=40,
                     vehicle_length=6,
                     spriterow_num=0)
    
    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=27,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist