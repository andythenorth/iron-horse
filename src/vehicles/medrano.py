from train import PassengerEngineConsist, MetroUnit

consist = PassengerEngineConsist(id='medrano',
                                 base_numeric_id=1490,
                                 name='Medrano',
                                 power=1100,
                                 intro_date=2000)

# should be 4 units, not 2
consist.add_unit(type=MetroUnit,
                 weight=30,
                 vehicle_length=8,
                 capacity=200,
                 spriterow_num=0)

consist.add_unit(type=MetroUnit,
                 weight=30,
                 vehicle_length=8,
                 capacity=200,
                 spriterow_num=1)
