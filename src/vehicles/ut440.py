from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='ut440',
                        base_numeric_id=440,
                        name='UT440',
                        power=900,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        intro_date=2011)

consist.add_unit(type=ElectricEngineUnit,
                 weight=40,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=ElectricEngineUnit,
                 weight=40,
                 vehicle_length=8,
                 spriterow_num=1)
