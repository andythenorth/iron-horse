import global_constants
from train import EngineConsist, MetroCargoUnit

consist = EngineConsist(id='tyburn',
                        base_numeric_id=2190,
                        title='Tyburn [Metro Train]',
                        track_type='METRO',
                        power=900,
                        speed=55,
                        type_base_buy_cost_points=56,  # dibble buy cost for game balance
                        intro_date=1950)

consist.add_unit(type=MetroCargoUnit,
                 weight=35,
                 vehicle_length=8,
                 capacity=60,
                 spriterow_num=0)

consist.add_unit(type=MetroCargoUnit,
                 weight=35,
                 vehicle_length=8,
                 capacity=60,
                 spriterow_num=1)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
