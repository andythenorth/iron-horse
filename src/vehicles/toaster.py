import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id='toaster',
                        base_numeric_id=990,
                        title='Toaster [Diesel]',
                        power=4200,
                        # dibble for game balance, assume super-slip control
                        tractive_effort_coefficient=0.4,
                        speed=110,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        vehicle_generation=6)

consist.add_unit(type=DieselLoco,
                 weight=140,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
