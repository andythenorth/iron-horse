import global_constants
from train import EngineConsist, SteamLoco

consist = EngineConsist(id = 'suburban',
              base_numeric_id = 1060,
              title = '2-6-2 Suburban [Steam]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 650,
              tractive_effort_coefficient = 0.2,
              speed = 70,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
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
                       spritesheet_suffix=1)
