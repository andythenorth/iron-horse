from train import PassengerEngineConsist, DieselEngineUnit

consist = PassengerEngineConsist(id='tin_rocket',
                                 base_numeric_id=530,
                                 title='Tin Rocket [Diesel]',
                                 power=600,
                                 speed=90,
                                 type_base_running_cost_points=-36,  # dibble running costs for game balance
                                 intro_date=1985)  # explicit intro date by design

consist.add_unit(type=DieselEngineUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=75,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
