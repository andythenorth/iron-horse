# coding=utf-8
import global_constants
from train import EngineConsist, DieselLoco
# for rest of stats, look up GE Evolution
consist = EngineConsist(id='evolucao',
                        base_numeric_id=200,
                        title='Evolução [Diesel]',
                        power=4400,
                        speed=75,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        intro_date=1995)

consist.add_unit(type=DieselLoco,
                 weight=40,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
