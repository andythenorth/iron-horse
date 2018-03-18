from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='ut440',
                        base_numeric_id=440,
                        title='UT440 [Electric]',
                        power=900,
                        speed=55,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=2011)

consist.add_unit(type=ElectricEngineUnit,
                 weight=40,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=ElectricEngineUnit,
                 weight=40,
                 vehicle_length=8,
                 spriterow_num=1)

