from train import EngineConsist, ElectroDieselEngineUnit

consist = EngineConsist(id='ultra_shoebox',
                        base_numeric_id=2170,
                        name='Ultra Shoebox',
                        role='branch',
                        power=1250,
                        power_by_railtype={'RAIL': 1250, 'ELRL': 2500},
                        type_base_buy_cost_points=0,  # dibble buy cost for game balance
                        type_base_running_cost_points=-28,  # dibble run cost for game balance
                        random_reverse=True,
                        gen=6)

consist.add_unit(type=ElectroDieselEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)

