import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id = 'kessler',
              base_numeric_id = 1990,
              title = '0-4-2 Kessler [Steam]',
              power = 450,
              track_type = 'NG',
              speed = 45,
              type_base_buy_cost_points = -10, # dibble buy cost for game balance
              type_base_running_cost_points = -7, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1860,
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 25,
                        vehicle_length = 5,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1,
                       visual_effect_offset='AUTOFLIP')
