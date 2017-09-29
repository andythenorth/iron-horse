import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id='suburban',
                        base_numeric_id=500,
                        title='2-6-2 Suburban [Steam]',
                        power=650,
                        tractive_effort_coefficient=0.2,
                        speed=80,
                        type_base_buy_cost_points=-2,  # dibble buy cost for game balance
                        type_base_running_cost_points=-6,  # dibble running costs for game balance
                        gen=2)

consist.add_unit(type=SteamLoco,
                 weight=57,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=1,
                          visual_effect_offset='AUTOFLIP')
