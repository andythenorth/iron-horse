import global_constants
from train import EngineConsist, MetroMultipleUnit

consist = EngineConsist(id = 'serpentine',
              base_numeric_id = 1500,
              title = 'Serpentine [Metro Train]',
              replacement_id = '-none',
              track_type = 'METRO',
              power = 600,
              speed = 40,
              buy_cost = 30,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1900,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

# should be 4 units not 2
consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        capacity_pax = 120,
                        spriterow_num = 0))

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        capacity_pax = 120,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
