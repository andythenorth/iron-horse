import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'tin_rocket',
              base_numeric_id = 1190,
              title = 'Tin Rocket [Diesel]',
              replacement_id = '-none',
              power = 750,
              speed = 100,
              type_base_running_cost_points = -36, # dibble running costs for game balance
              intro_date = 1998,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = False)

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 65,
                        vehicle_length = 8,
                        capacity_pax = 75,
                        capacity_mail = 40,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
