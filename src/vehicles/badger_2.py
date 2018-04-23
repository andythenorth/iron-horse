from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='badger_2',
                        base_numeric_id=2180,
                        name='Flying Badger 2',
                        role='express_2',
                        power=7400,
                        speed=140,
                        type_base_buy_cost_points=63,  # dibble buy cost for game balance
                        random_reverse=True,
                        gen=6)

consist.add_unit(type=ElectricEngineUnit,
                 weight=82,
                 vehicle_length=8,
                 spriterow_num=0)

