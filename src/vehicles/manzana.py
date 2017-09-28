import global_constants
from train import EngineConsist, MetroPaxUnit

consist = EngineConsist(id='manzana',
                        base_numeric_id=1480,
                        title='Manzana [Metro Train]',
                        track_type='METRO',
                        power=900,
                        speed=55,
                        type_base_buy_cost_points=60,  # dibble buy cost for game balance
                        intro_date=1950)

# should be 4 units not 2
consist.add_unit(type=MetroPaxUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity_pax=160,
                 spriterow_num=0)

consist.add_unit(type=MetroPaxUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity_pax=160,
                 spriterow_num=1)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date)
