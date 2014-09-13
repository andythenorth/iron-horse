import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id = 'suburban',
              base_numeric_id = 1060,
              title = '2-6-2 Suburban [Steam]',
              replacement_id = '-none',
              power = 650,
              tractive_effort_coefficient = 0.2,
              speed = 70,
              type_base_running_cost_points = -6, # dibble running costs for game balance
              vehicle_life = 40,
              intro_date = 1930,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 57,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1,
                       visual_effect_offset='AUTOFLIP')

