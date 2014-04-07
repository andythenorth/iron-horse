import global_constants
from train import EngineConsist, MetroMultipleUnit

consist = EngineConsist(id = 'westbourne',
              base_numeric_id = 1510,
              title = 'Westbourne [Metro Train]',
              replacement_id = '-none',
              track_type = 'METRO',
              power = 900,
              speed = 55,
              buy_cost = 67,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              intro_date = 1950,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

# should be 4 units not 2
consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        capacity_pax = 160,
                        spriterow_num = 0))

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 40,
                        vehicle_length = 8,
                        capacity_pax = 160,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
