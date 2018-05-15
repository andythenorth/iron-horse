from train import PassengerEngineConsist, MetroUnit

consist = PassengerEngineConsist(id='manzana',
                                 base_numeric_id=1480,
                                 name='Manzana',
                                 track_type='METRO',
                                 power=900,
                                 type_base_buy_cost_points=60,  # dibble buy cost for game balance
                                 intro_date=1950)

# should be 4 units not 2
consist.add_unit(type=MetroUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=160,
                 spriterow_num=0)

consist.add_unit(type=MetroUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=160,
                 spriterow_num=1)
