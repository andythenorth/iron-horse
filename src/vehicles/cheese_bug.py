from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='cheese_bug',
                        base_numeric_id=490,
                        name='0-6-2 Cheese Bug',
                        role='universal',
                        track_type='NG',
                        power=350,
                        tractive_effort_coefficient=0.2,
                        type_base_buy_cost_points=-5,  # dibble buy cost for game balance
                        type_base_running_cost_points=0,  # dibble running costs for game balance
                        intro_date=1860)

consist.add_unit(type=SteamEngineUnit,
                 weight=30,
                 vehicle_length=4,
                 spriterow_num=0)
