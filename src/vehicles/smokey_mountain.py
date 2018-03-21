from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='smokey_mountain',
                        base_numeric_id=1610,
                        name='Smokey Mountain',
                        power=3200,
                        type_base_buy_cost_points=24,  # dibble buy cost for game balance
                        type_base_running_cost_points=20,  # dibble run cost for game balance
                        speed=55,
                        intro_date=1950)

consist.add_unit(type=DieselEngineUnit,
                 weight=112,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=DieselEngineUnit,
                 weight=112,
                 vehicle_length=8,
                 spriterow_num=1)

