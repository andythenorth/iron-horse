from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='wizzo',
                        base_numeric_id=420,
                        title='Wizzo [Diesel]',
                        power=2200,
                        speed=110,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        type_base_running_cost_points=30,  # dibble running costs for game balance
                        gen=4)

consist.add_unit(type=DieselEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
