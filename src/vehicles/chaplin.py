from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='chaplin',
                        base_numeric_id=110,
                        name='2-4-0 Chaplin',
                        role='branch',
                        power=500,
                        tractive_effort_coefficient=0.2,
                        speed=60,
                        type_base_buy_cost_points=-3,  # dibble buy cost for game balance
                        random_reverse=True,
                        gen=1)

consist.add_unit(type=SteamEngineUnit,
                 weight=35,
                 vehicle_length=6,
                 spriterow_num=0)

