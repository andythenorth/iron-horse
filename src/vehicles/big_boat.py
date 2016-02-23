import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'big_boat',
              base_numeric_id = 1600,
              title = 'Big Boat [Diesel]',
              replacement_id = '-none',
              power = 4500,
              tractive_effort_coefficient = 0.35, # dibble up TE, modern diesels can cheat adhesion using wheel slip
              speed = 75,
              vehicle_life = 40,
              intro_date = 1985)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 190,
                        vehicle_length = 10,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
