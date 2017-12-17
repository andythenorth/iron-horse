from train import EngineConsist, DieselLoco

consist = EngineConsist(id='donegal',
                        base_numeric_id=140,
                        title='Donnegal [Diesel]',
                        track_type='NG',
                        power=250,
                        speed=55,
                        type_base_buy_cost_points=-18,  # dibble buy cost for game balance
                        type_base_running_cost_points=-30,  # dibble running costs for game balance
                        intro_date=1954)

consist.add_unit(type=DieselLoco,
                 weight=20,
                 vehicle_length=7,
                 capacity=35,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
