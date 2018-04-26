from train import PassengerEngineConsist, ElectricPaxUnit

consist = PassengerEngineConsist(id='pendolino_thing',
                                 base_numeric_id=980,
                                 name='Blaze',
                                 role='pax_high_speed',
                                 power=1900,
                                 type_base_running_cost_points=-32,  # dibble running costs for game balance
                                 intro_date=2000)  # explicit intro date by design

# 4 units (2-tiles) because building these is annoying if the units are too small?
# or 2 units (1-tile) to make any integer length?

consist.add_unit(type=ElectricPaxUnit,
                 weight=41,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0)

consist.add_unit(type=ElectricPaxUnit,
                 weight=41,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0)

