from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='moor_gallop',
                        base_numeric_id=170,
                        name='Moor Gallop',
                        role='express_2',
                        power=2400,
                        tractive_effort_coefficient=0.25,
                        type_base_buy_cost_points=10,  # dibble buy cost for game balance
                        gen=3,
                        intro_date_offset=5) # introduce later than gen epoch by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=105,
                 vehicle_length=8,
                 spriterow_num=0)

