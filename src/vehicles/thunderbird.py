import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id='thunderbird',
                        base_numeric_id=3090,
                        title='Thunderbird [Diesel]',
                        power=2650,
                        speed=125,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        type_base_running_cost_points=30,  # dibble running costs for game balance
                        gen=5)

consist.add_unit(type=DieselLoco,
                 weight=90,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
