from train import PassengerEngineConsist, MetroUnit

consist = PassengerEngineConsist(id='fleet',
                                 base_numeric_id=210,
                                 name='Fleet',
                                 role='pax_metro',
                                 track_type='METRO',
                                 power=1100,
                                 speed=65,
                                 type_base_buy_cost_points=80,  # dibble buy cost for game balance
                                 intro_date=2000)

# should be 4 short units, not 2 long but eh
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

