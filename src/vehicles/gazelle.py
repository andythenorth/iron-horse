import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id='gazelle',
                        base_numeric_id=2030,
                        title='Gazelle [Diesel]',
                        power=1800,
                        track_type='NG',
                        speed=85,
                        intro_date=1975)

consist.add_unit(type=DieselLoco,
                 weight=90,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
