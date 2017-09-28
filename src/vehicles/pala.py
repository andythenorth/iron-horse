import global_constants
from train import EngineConsist, DieselLoco
# standard gauge GE Shovelnose
consist = EngineConsist(id = 'pala',
              base_numeric_id = 320,
              title = 'Pala [Diesel]',
              power = 1200,
              speed = 75,
              vehicle_life = 30,
              intro_date = 1955)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 105,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
