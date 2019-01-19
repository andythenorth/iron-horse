from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

def main():    
    consist = EngineConsist(id='lemon',
                            base_numeric_id=270,
                            name='4-8-0 Lemon',
                            role='heavy_freight_1',
                            power=2400,
                            tractive_effort_coefficient=0.29,
                            buy_cost=114,
                            gen=3)
    
    consist.add_unit(type=SteamEngineUnit,
                     weight=115,
                     vehicle_length=8,
                     spriterow_num=0)
    
    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=50,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist