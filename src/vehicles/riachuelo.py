from train import PassengerEngineConsist, MetroUnit

consist = PassengerEngineConsist(id='riachuelo',
                                 base_numeric_id=1470,
                                 name='Riachuelo',
                                 power=600,
                                 intro_date=1900)

# should be 4 units not 2
consist.add_unit(type=MetroUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=120,
                 spriterow_num=0)

consist.add_unit(type=MetroUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=120,
                 spriterow_num=1)
