from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='planet',
                        base_numeric_id=360,
                        title='Planet [Diesel]',
                        track_type='NG',
                        power=500,
                        speed=55,
                        type_base_buy_cost_points=-20,  # dibble buy cost for game balance
                        type_base_running_cost_points=-20,  # dibble running costs for game balance
                        intro_date=1950)

consist.add_unit(type=DieselEngineUnit,
                 weight=40,
                 vehicle_length=4,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
