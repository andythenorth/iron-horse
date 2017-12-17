from train import PassengerEngineConsist, DieselLoco

consist = PassengerEngineConsist(id='happy_train',
                                 base_numeric_id=100,
                                 title='Happy Train [Diesel]',
                                 power=750,
                                 # matched to fast (in this gen) freight speeds
                                 speed=110,
                                 type_base_running_cost_points=-36,  # dibble running costs for game balance
                                 intro_date=2015)  # explicit intro date by design

consist.add_unit(type=DieselLoco,
                 weight=40,
                 vehicle_length=8,
                 capacity=75,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
