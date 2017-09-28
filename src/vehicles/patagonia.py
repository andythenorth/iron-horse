import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id='patagonia',
                        base_numeric_id=330,
                        title='Patagonia [Diesel]',
                        track_type='NG',
                        power=500,
                        speed=55,
                        type_base_buy_cost_points=-18,  # dibble buy cost for game balance
                        type_base_running_cost_points=-30,  # dibble running costs for game balance
                        intro_date=1960)

consist.add_unit(type=DieselRailcar,
                 weight=20,
                 vehicle_length=7,
                 capacity_pax=35,
                 spriterow_num=0)

consist.add_unit(type=DieselRailcar,
                 weight=20,
                 vehicle_length=7,
                 capacity_pax=35,
                 spriterow_num=1)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
