import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'planet',
              base_numeric_id = 1560,
              title = 'Planet [Diesel]',
              replacement_id = '-none',
              track_type = 'NG',
              power = 500,
              speed = 55,
              type_base_buy_cost_points = -20, # dibble buy cost for game balance
              type_base_running_cost_points = -20, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1950,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 4,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
