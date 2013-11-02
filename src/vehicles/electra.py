import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'electra',
              base_numeric_id = 1090,
              title = 'Electra [Electric]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 2400,
              tractive_effort_coefficient = 0.32,
              speed = 90,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1953,
              graphics_status = '')
              
consist.add_unit(ElectricLoco(consist = consist,
                        weight = 105,
                        vehicle_length = 8,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
