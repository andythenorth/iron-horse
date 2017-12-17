from train import PassengerEngineConsist, ElectricPaxUnit

consist = PassengerEngineConsist(id='velaro_thing',
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
                 capacity=40,
                 spriterow_num=0)

consist.add_unit(type=ElectricPaxUnit,
                 weight=55,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
