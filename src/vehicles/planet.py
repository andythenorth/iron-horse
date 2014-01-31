import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'planet',
              base_numeric_id = 1560,
              title = 'Planet [Diesel]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              track_type = 'NG',
              power = 500,
              speed = 55,
              buy_cost = 29,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1950,
              graphics_status = '',
              use_legacy_spritesheet = True)
              
consist.add_unit(DieselLoco(consist = consist,
                        weight = 40,
                        vehicle_length = 7,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
