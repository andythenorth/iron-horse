from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='dragon',
                        base_numeric_id=420,
                        name='Dragon',
                        role='express_1',
                        power=2200,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        type_base_running_cost_points=30,  # dibble running costs for game balance
                        random_reverse=True,
                        gen=4)

consist.add_unit(type=DieselEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=0)

