import global_constants
from train import EngineConsist, MetroMultipleUnit

consist = EngineConsist(id = 'medrano',
              base_numeric_id = 1490,
              title = 'Medrano [Metro Train]',
              replacement_id = '-none',
              track_type = 'METRO',
              power = 1100,
              speed = 65,
              type_base_buy_cost_points = 80, # dibble buy cost for game balance
              intro_date = 2000,
              vehicle_life = 40,
              use_legacy_spritesheet = True)

# should be 4 units, not 2
consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_pax = 200,
                        spriterow_num = 0))

consist.add_unit(MetroMultipleUnit(consist = consist,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_pax = 200,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
