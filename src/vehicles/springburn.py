import global_constants
from train import EngineConsist, DieselLoco

consist = EngineConsist(id = 'springburn',
              base_numeric_id = 1790,
              title = 'Springburn [Diesel]',
              power = 1200,
              type_base_running_cost_points = -20, # dibble run cost for game balance
              speed = 55,
              vehicle_life = 40,
              intro_date = 1950,
              use_legacy_spritesheet = True)

consist.add_unit(DieselLoco(consist = consist,
                        weight = 80,
                        vehicle_length = 6,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
