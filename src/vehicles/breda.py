from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='breda',
                        base_numeric_id=80,
                        name='Breda E32',
                        power=900,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1961)

consist.add_unit(type=ElectricEngineUnit,
                 weight=40,
                 vehicle_length=8,
                 spriterow_num=0)

