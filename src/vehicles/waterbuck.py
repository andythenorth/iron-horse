import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id='waterbuck',
                        base_numeric_id=2020,
                        title='Waterbuck [Diesel]',
                        power=2200,
                        track_type='NG',
                        speed=65,
                        type_base_running_cost_points=-2,  # dibble running costs for game balance
                        intro_date=1990)

consist.add_unit(type=DieselLoco,
                 weight=120,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
