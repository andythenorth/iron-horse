import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id = 'chaplin',
              base_numeric_id = 1010,
              title = '2-4-0 Chaplin [Steam]',
              replacement_id = '-none',
              power = 450,
              tractive_effort_coefficient = 0.2,
              speed = 60,
              type_base_buy_cost_points = -3, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 1860,
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 35,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1,
                       visual_effect_offset='AUTOFLIP')
