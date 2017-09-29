import global_constants
from train import EngineConsist, MetroPaxUnit

consist = EngineConsist(id='serpentine',
                        base_numeric_id=460,
                        title='Serpentine [Metro Train]',
                        track_type='METRO',
                        power=600,
                        speed=40,
                        type_base_buy_cost_points=40,  # dibble buy cost for game balance
                        intro_date=1900)

# should be 4 units not 2, would look nicer short
consist.add_unit(type=MetroPaxUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity_pax=120,
                 spriterow_num=0)

consist.add_unit(type=MetroPaxUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity_pax=120,
                 spriterow_num=1)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
