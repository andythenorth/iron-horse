import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'hudswell',
              base_numeric_id = 1550,
              title = 'Hudswell [Steam]',
              replacement_id = '-none',
              track_type = 'NG',
              power = 800,
              tractive_effort_coefficient = 0.2,
              speed = 50,
              type_base_buy_cost_points = -11, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 1910,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 50,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
