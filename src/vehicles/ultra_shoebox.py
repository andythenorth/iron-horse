from train import EngineConsist, ElectroDieselEngineUnit

consist = EngineConsist(id='ultra_shoebox',
                        base_numeric_id=2170,
                        name='Ultra Shoebox',
                        role='branch_express',
                        power=1450,  # a bit higher than progression would require, to support higher speed
                        power_by_railtype={'RAIL': 1450, 'ELRL': 2600},
                        type_base_buy_cost_points=0,  # dibble buy cost for game balance
                        type_base_running_cost_points=-28,  # dibble run cost for game balance
                        random_reverse=True,
                        gen=6)

consist.add_unit(type=ElectroDieselEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)
