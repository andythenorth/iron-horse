from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='pequeno',
                        base_numeric_id=350,
                        name='0-4-0 Pequeno',
                        power=350,
                        track_type='NG',
                        speed=35,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1865)

consist.add_unit(type=SteamEngineUnit,
                 weight=40,
                 vehicle_length=4,
                 spriterow_num=0)

