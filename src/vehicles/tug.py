import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id='tug',
                        base_numeric_id=220,
                        title='Tug [Diesel]',
                        power=3600,
                        # dibble for game balance, assume super-slip control
                        tractive_effort_coefficient=0.4,
                        speed=85,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        gen=5)

consist.add_unit(type=DieselLoco,
                 weight=125,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
