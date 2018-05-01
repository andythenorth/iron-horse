from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='freight_tank',
                        base_numeric_id=1330,
                        name='2-8-2 Gwynt',
                        role='branch_freight',
                        power=1000,
                        type_base_buy_cost_points=-2,  # dibble buy cost for game balance
                        type_base_running_cost_points=-6,  # dibble running costs for game balance
                        random_reverse=True,
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)

