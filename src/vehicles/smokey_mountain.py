from train import EngineConsist, DieselLoco

consist = EngineConsist(id='smokey_mountain',
                        base_numeric_id=1610,
                        title='Smokey Mountain [Diesel]',
                        power=3200,
                        type_base_buy_cost_points=24,  # dibble buy cost for game balance
                        type_base_running_cost_points=20,  # dibble run cost for game balance
                        speed=55,
                        intro_date=1950)

consist.add_unit(type=DieselLoco,
                 weight=112,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=DieselLoco,
                 weight=112,
                 vehicle_length=8,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
