import global_constants
from train import EngineConsist, ElectroDieselLoco

consist = EngineConsist(id = 'double_juice',
              base_numeric_id = 160,
              title = 'Double Juice [ElectroDiesel]',
              power = 6750,
              tractive_effort_coefficient = 0.4, #dibble for game balance, assume super-slip control
              speed = 100,
              type_base_buy_cost_points = 60, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 2000,
              power_by_railtype = {'RAIL': 3750, 'ELRL': 6750})

consist.add_unit(ElectroDieselLoco(consist = consist,
                        weight = 120,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date)
