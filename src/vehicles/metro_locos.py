import global_constants
from train import EngineConsist, MetroLoco

consist = EngineConsist(id = 'metro_loco_brit_gen_1',
              base_numeric_id = 1190,
              title = 'Metro Loco [Electric]',
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

consist.add_unit(MetroLoco(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_freight = 30,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=1986,
                       spritesheet_suffix=0)
