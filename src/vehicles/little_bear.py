import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'little_bear',
              base_numeric_id = 1160,
              title = 'Little Bear [Diesel]',
              replacement_id = '-none',
              power = 750,
              speed = 85,
              type_base_buy_cost_points = 5, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 1964,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 54,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
