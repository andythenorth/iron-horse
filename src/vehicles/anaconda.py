import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id='anaconda',
                        base_numeric_id=30,
                        title='Anaconda [Diesel]',
                        power=300,
                        speed=75,
                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                        intro_date=1980)

consist.add_unit(type=DieselRailcar,
                 weight=65,
                 vehicle_length=8,
                 capacity_pax=55,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
