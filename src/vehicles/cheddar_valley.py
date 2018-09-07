from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='cheddar_valley',
                        base_numeric_id=220,
                        name='Cheddar Valley',
                        role='heavy_freight_1',
                        power=3600,
                        # dibble for game balance, assume super-slip control
                        tractive_effort_coefficient=0.4,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        random_reverse=True,
                        gen=5,
                        sprites_complete=True)

consist.add_unit(type=DieselEngineUnit,
                 weight=125,
                 vehicle_length=8,
                 spriterow_num=0)
