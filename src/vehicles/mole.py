import global_constants
from train import EngineConsist, MetroCargoUnit

consist = EngineConsist(id = 'mole',
              base_numeric_id = 290,
              title = 'Mole [Metro Train]',
              replacement_id = '-none',
              track_type = 'METRO',
              power = 600,
              speed = 40,
              type_base_buy_cost_points = 36, # dibble buy cost for game balance
              intro_date = 1900,
              vehicle_life = 40,
              use_legacy_spritesheet = True)

consist.add_unit(MetroCargoUnit(consist = consist,
                        weight = 35,
                        vehicle_length = 8,
                        capacity_mail = 60,
                        spriterow_num = 0))

consist.add_unit(MetroCargoUnit(consist = consist,
                        weight = 35,
                        vehicle_length = 8,
                        capacity_mail = 60,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
