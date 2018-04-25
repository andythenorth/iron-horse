from train import EngineConsist, DieselEngineUnit
# class 70-ish thing
consist = EngineConsist(id='chimera',
                        base_numeric_id=990,
                        name='Chimera',
                        role='heavy_freight',
                        power=4200,
                        # dibble for game balance, assume super-slip control
                        tractive_effort_coefficient=0.4,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        random_reverse=True,
                        gen=6)

consist.add_unit(type=DieselEngineUnit,
                 weight=140,
                 vehicle_length=8,
                 spriterow_num=0)

