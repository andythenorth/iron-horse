from train import EngineConsist, SteamEngineUnit

def main():    
    consist = EngineConsist(id='milne',
                            base_numeric_id=2050,
                            name='4-8-2 Milne',
                            power=600,
                            base_track_type='NG',
                            random_reverse=True,
                            intro_date=1910)
    
    consist.add_unit(type=SteamEngineUnit,
                     weight=50,
                     vehicle_length=7,
                     spriterow_num=0)

    return consist