import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'thing_5',
              base_numeric_id = 2050,
              title = '4-6-0 Thing 5 [Steam]',
              replacement_id = '-none',
              power = 900,
              track_type = 'NG',
              speed = 55,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              type_base_running_cost_points = -15, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1955,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
