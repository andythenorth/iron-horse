import global_constants
from train import EngineConsist, ElectroDieselLoco

consist = EngineConsist(id='super_shoebox',
                        base_numeric_id=880,
                        title='Super Shoebox [ElectroDiesel]',
                        power=1100,
                        speed=125,
                        type_base_buy_cost_points=0,  # dibble buy cost for game balance
                        type_base_running_cost_points=-28,  # dibble run cost for game balance
                        gen=5,
                        power_by_railtype={'RAIL': 1100, 'ELRL': 2200})

consist.add_unit(type=ElectroDieselLoco,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
