import global_constants
from train import EngineConsist, ElectricPaxUnit

consist = EngineConsist(id='velaro_thing',
                        base_numeric_id=130,
                        title='Velaro Thing [Electric]',
                        power=2600,
                        speed=200,
                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                        intro_date=2020)  # explicit intro date by design

# 4 units (2-tiles) because building these is annoying if the units are too small?
# or 2 units (1-tile) to make any integer length?

consist.add_unit(type=ElectricPaxUnit,
                 weight=55,
                 vehicle_length=8,
                 capacity_pax=40,
                 spriterow_num=0)

consist.add_unit(type=ElectricPaxUnit,
                 weight=55,
                 vehicle_length=8,
                 capacity_pax=40,
                 spriterow_num=0)

consist.add_model_variant(start_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
