import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'screamer',
              base_numeric_id = 1130,
              title = 'Screamer [Electric]',
              replacement_id = '-none',
              power = 6400,
              speed = 155,
              buy_cost = 147,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1990,
              graphics_status = '',
              use_legacy_spritesheet = True)
              
consist.add_unit(ElectricLoco(consist = consist,
                        weight = 90,
                        vehicle_length = 8,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
