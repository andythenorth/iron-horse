from train import EngineConsist, DieselLoco

consist = EngineConsist(id='turtle',
                        base_numeric_id=3150,
                        title='Turtle [Diesel]',
                        power=3450,
                        speed=125,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        type_base_running_cost_points=30,  # dibble running costs for game balance
                        gen=6)

consist.add_unit(type=DieselLoco,
                 weight=95,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
