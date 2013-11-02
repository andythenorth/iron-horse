import global_constants
from train import EngineConsist, ElectroDieselLoco

# also needs to set 1250hp for diesel mode

consist = EngineConsist(id = 'double_juice',
              base_numeric_id = 1150,
              title = 'Double Juice [ElectroDiesel]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 5000,
              speed = 100,
              buy_cost = 22,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 2012,
              graphics_status = '')
              
consist.add_unit(ElectroDieselLoco(consist = consist,
                        weight = 90,
                        vehicle_length = 7,
                        spriterow_num = 0))              

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
