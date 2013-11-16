import global_constants
from train import EngineConsist, MetroMultipleUnit

consist = EngineConsist(id = 'metro_mu_brit_gen_1',
              base_numeric_id = 1160,
              title = '1900 Metro Train [Electric]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 450,
              speed = 75,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1960,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_freight = 30,
                        spriterow_num = 0),
                        repeat=2)              

consist.add_model_variant(intro_date=0,
                       end_date=1986,
                       spritesheet_suffix=0)


consist = EngineConsist(id = 'metro_mu_brit_gen_2',
              base_numeric_id = 1170,
              title = '1950 Metro Train [Electric]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 450,
              speed = 75,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1960,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_freight = 30,
                        spriterow_num = 0),
                        repeat=2)              

consist.add_model_variant(intro_date=0,
                       end_date=1986,
                       spritesheet_suffix=0)


consist = EngineConsist(id = 'metro_mu_brit_gen_3',
              base_numeric_id = 1180,
              title = '2000 Metro Train [Electric]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 450,
              speed = 75,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1960,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_freight = 30,
                        spriterow_num = 0),
                        repeat=2)              

consist.add_model_variant(intro_date=0,
                       end_date=1986,
                       spritesheet_suffix=0)
