import global_constants
from train import EngineConsist, MetroMultipleUnit

consist = EngineConsist(id = 'metro_mu_brit_extras_gen_1',
              base_numeric_id = 1500,
              title = '1900 Metro Train [Electric]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 600,
              speed = 40,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1900,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        capacity_pax = 100,
                        spriterow_num = 0),
                        repeat=2)              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = EngineConsist(id = 'metro_mu_brit_extras_gen_2',
              base_numeric_id = 1510,
              title = '1950 Metro Train [Electric]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 900,
              speed = 55,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1950,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        capacity_pax = 100,
                        spriterow_num = 0),
                        repeat=2)              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = EngineConsist(id = 'metro_mu_brit_extras_gen_3',
              base_numeric_id = 1520,
              title = '2000 Metro Train [Electric]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 1100,
              speed = 65,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 2000,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_pax = 100,
                        spriterow_num = 0),
                        repeat=2)              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
