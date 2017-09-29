import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id='walker',
                        base_numeric_id=430,
                        title='Walker [Diesel]',
                        power=900,
                        track_type='NG',
                        speed=55,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1955)

consist.add_unit(type=DieselLoco,
                 weight=40,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
