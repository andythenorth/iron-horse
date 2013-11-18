import global_constants
from train import EngineConsist, MetroLoco

consist = EngineConsist(id = 'metro_loco_brit_extras_gen_1',
              base_numeric_id = 1530,
              title = 'Metro Loco [Battery]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 800,
              speed = 45,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1900,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(MetroLoco(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
