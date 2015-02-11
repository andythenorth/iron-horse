import global_constants
from train import EngineConsist, MetroLoco

consist = EngineConsist(id = 'mole',
              base_numeric_id = 1530,
              title = 'Mole [Metro Train]',
              replacement_id = '-none',
              track_type = 'METRO',
              power = 800,
              speed = 45,
              type_base_buy_cost_points = 10, # dibble buy cost for game balance
              intro_date = 1900,
              vehicle_life = 40,
              use_legacy_spritesheet = True)

consist.add_unit(MetroLoco(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
