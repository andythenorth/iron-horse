from train import PassengerEngineConsist, MetroUnit

consist = PassengerEngineConsist(id='fleet',
                                 base_numeric_id=210,
                                 name='Fleet',
                                 role='pax_metro',
                                 track_type='METRO',
                                 power=1100,
                                 type_base_buy_cost_points=80,  # dibble buy cost for game balance
                                 gen=5,
                                 intro_date_offset=10) # introduce later than gen epoch by design

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

