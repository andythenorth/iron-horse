from train import PassengerEngineConsist, MetroUnit

consist = PassengerEngineConsist(id='westbourne',
                                 base_numeric_id=360,
                                 name='Westbourne',
                                 role='pax_metro',
                                 track_type='METRO',
                                 power=900,
                                 type_base_buy_cost_points=60,  # dibble buy cost for game balance
                                 gen=3,
                                 intro_date_offset=20) # introduce later than gen epoch by design

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

