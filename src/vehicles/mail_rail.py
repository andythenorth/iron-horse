import global_constants
from train import EngineConsist, DieselRailcarMail

consist = EngineConsist(id='mail_rail',
                        base_numeric_id=3000,
                        title='Mail Rail [Diesel]',
                        power=870,
                        speed=110,  # matched to fast (in this gen) freight speeds
                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                        intro_date=2015)  # explicit intro date by design

consist.add_unit(type=DieselRailcarMail,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=3)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
