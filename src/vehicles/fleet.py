import global_constants
from train import EngineConsist, MetroMultipleUnit

consist = EngineConsist(id = 'fleet',
              base_numeric_id = 1520,
              title = 'Fleet [Metro Train]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              track_type = 'METRO',
              power = 1100,
              speed = 65,
              buy_cost = 88,
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
                        spriterow_num = 0))

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_pax = 100,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
