from train import PassengerEngineConsist, MetroUnit

consist = PassengerEngineConsist(id='serpentine',
                                 base_numeric_id=460,
                                 title='Serpentine [Metro Train]',
                                 track_type='METRO',
                                 power=600,
                                 speed=40,
                                 type_base_buy_cost_points=40,  # dibble buy cost for game balance
                                 intro_date=1900)

# should be 4 units not 2, would look nicer short
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

