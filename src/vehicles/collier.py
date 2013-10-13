import global_constants
from train import Consist, SteamLoco

consist = Consist(id = 'collier',
              base_numeric_id = 1240,
              title = 'Collier [Steam]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1900,
              graphics_status = '')
              
consist.add_vehicle(SteamLoco(consist = consist,
                        speed = 45,
                        power = 1300,
                        weight = 95,
                        vehicle_length = 7,
                        loading_speed = 20))              

consist.add_vehicle(SteamLoco(consist = consist,
                        speed = 45,
                        power = 1300,
                        weight = 95,
                        vehicle_length = 7,
                        loading_speed = 20))              

consist.add_vehicle(vehicle = SteamLoco(consist = consist,
                        speed = 45,
                        power = 1300,
                        weight = 95,
                        vehicle_length = 7,
                        loading_speed = 20),
                    repeat = 2)              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
