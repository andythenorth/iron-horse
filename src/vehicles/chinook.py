from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='chinook',
                        base_numeric_id=120,
                        name='Chinook',
                        role='heavy_freight',
                        power=3000,
                        speed=75,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        gen=4)

consist.add_unit(type=DieselEngineUnit,
                 weight=80,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_unit(type=DieselEngineUnit,
                 weight=80,
                 vehicle_length=6,
                 spriterow_num=1)

