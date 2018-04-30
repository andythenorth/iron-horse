from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='phoenix',
                        base_numeric_id=160,
                        name='Phoenix',
                        role='freight',
                        power=1900,
                        type_base_buy_cost_points=60,  # dibble buy cost for game balance
                        random_reverse=True,
                        gen=6)

consist.add_unit(type=DieselEngineUnit,
                 weight=120,
                 vehicle_length=8,
                 spriterow_num=0)

