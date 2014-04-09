import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'collier',
              base_numeric_id = 1030,
              title = '0-8-0 Collier [Steam]',
              replacement_id = '-none',
              power = 1300,
              tractive_effort_coefficient = 0.29,
              speed = 45,
              type_base_buy_cost_points = -13, # dibble buy cost for game balance
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1900,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 95,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 35,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
