import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'raven',
              base_numeric_id = 390,
              title = 'Raven [Electric]',
              power = 1800,
              tractive_effort_coefficient = 0.32,
              speed = 80,
              buy_cost = 77,
              vehicle_life = 40,
              intro_date = 1919,
              use_legacy_spritesheet = True)

consist.add_unit(ElectricLoco(consist = consist,
                        weight = 120,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
