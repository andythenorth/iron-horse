import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'tin_rocket',
              base_numeric_id = 1210,
              title = 'Tin Rocket [Diesel]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 450,
              speed = 85,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1997,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_pax = 75,
                        capacity_mail = 40,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
