import global_constants
from train import EngineConsist, MetroCargoUnit

consist = EngineConsist(id = 'tideway',
              base_numeric_id = 2200,
              title = 'Tideway [Metro Train]',
              track_type = 'METRO',
              power = 1100,
              speed = 65,
              type_base_buy_cost_points = 36, # dibble buy cost for game balance
              intro_date = 2000)

consist.add_unit(MetroCargoUnit(consist = consist,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_mail = 60,
                        spriterow_num = 0))

consist.add_unit(MetroCargoUnit(consist = consist,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_mail = 60,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
