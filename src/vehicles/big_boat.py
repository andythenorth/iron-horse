import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'big_boat',
              base_numeric_id = 1600,
              title = 'Big Boat [Diesel]',
              power = 4500,
              tractive_effort_coefficient = 0.35, # dibble up TE, modern diesels can cheat adhesion using wheel slip
              speed = 75,
              intro_date = 1985)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 190,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)

# I tried the Big Boat with a long-hood forward random variant, but it looked bad, removed it.
