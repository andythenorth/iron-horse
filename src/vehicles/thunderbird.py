from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='thunderbird',
                        base_numeric_id=3090,
                        name='Thunderbird',
                        power=2650,
                        speed=125,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        type_base_running_cost_points=30,  # dibble running costs for game balance
                        gen=5)

consist.add_unit(type=DieselEngineUnit,
                 weight=90,
                 vehicle_length=8,
                 spriterow_num=0)

