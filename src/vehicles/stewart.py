import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'stewart',
              base_numeric_id = 1540,
              title = 'Stewart [Steam]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              track_type = 'NG',
              power = 350,
              tractive_effort_coefficient = 0.2,
              speed = 40,
              buy_cost = 10,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1860,
              graphics_status = '',
              use_legacy_spritesheet = True)
              
consist.add_unit(SteamLoco(consist = consist,
                        weight = 35,
                        vehicle_length = 6,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
