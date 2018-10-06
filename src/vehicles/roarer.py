from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='roarer',
                        base_numeric_id=2230,
                        name='Roarer',
                        role='express_2',
                        power=3200,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        random_reverse=True,
                        gen=4,
                        pantograph_type='z-shaped-double',
                        intro_date_offset=5)  # introduce later than gen epoch by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=0)
