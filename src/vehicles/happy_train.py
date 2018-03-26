from train import PassengerEngineConsist, DieselEngineUnit

consist = PassengerEngineConsist(id='happy_train',
                                 base_numeric_id=100,
                                 name='Happy Train',
                                 role='pax_railcar',
                                 power=750,
                                 # matched to fast (in this gen) freight speeds
                                 speed=110,
                                 type_base_running_cost_points=-36,  # dibble running costs for game balance
                                 intro_date=2015)  # explicit intro date by design

consist.add_unit(type=DieselEngineUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=75,
                 spriterow_num=0)

