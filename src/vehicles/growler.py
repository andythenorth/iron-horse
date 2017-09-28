import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id='growler',
                        base_numeric_id=2240,
                        title='Growler [Diesel]',
                        power=1550,
                        speed=75,
                        vehicle_generation=4)

consist.add_unit(type=DieselLoco,
                 weight=100,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
