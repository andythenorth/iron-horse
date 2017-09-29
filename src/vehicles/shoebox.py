import global_constants
from train import EngineConsist, ElectroDieselLoco

consist = EngineConsist(id='shoebox',
                        base_numeric_id=280,
                        title='Shoebox [ElectroDiesel]',
                        power=950,
                        speed=110,
                        type_base_buy_cost_points=0,  # dibble buy cost for game balance
                        type_base_running_cost_points=-28,  # dibble run cost for game balance
                        gen=4,
                        power_by_railtype={'RAIL': 950, 'ELRL': 1800})

consist.add_unit(type=ElectroDieselLoco,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
