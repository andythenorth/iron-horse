from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

def main():    
    consist = EngineConsist(id='americano',
                            base_numeric_id=20,
                            name='4-4-0 Americano',
                            power=1000,
                            intro_date=1850)
    
    consist.add_unit(type=SteamEngineUnit,
                     weight=52,
                     vehicle_length=5,
                     spriterow_num=0)
    
    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=30,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist