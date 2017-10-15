import global_constants
from train import EngineConsist, DieselRailcarPassenger

consist = EngineConsist(id='happy_train',
                        base_numeric_id=100,
                        title='Happy Train [Diesel]',
                        power=750,
                        speed=100,  # matched to freight speeds
                        type_base_running_cost_points=-36,  # dibble running costs for game balance
                        intro_date=2015)  # explicit intro date by design

consist.add_unit(type=DieselRailcarPassenger,
                 weight=40,
                 vehicle_length=8,
                 capacity=75,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
