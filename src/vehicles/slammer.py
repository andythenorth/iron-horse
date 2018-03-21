from train import PassengerEngineConsist, DieselEngineUnit

consist = PassengerEngineConsist(id='slammer',
                                 base_numeric_id=470,
                                 title='Slammer',
                                 power=300,
                                 speed=75,
                                 type_base_running_cost_points=-32,  # dibble running costs for game balance
                                 intro_date=1955)  # explicit intro date by design

consist.add_unit(type=DieselEngineUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0)

