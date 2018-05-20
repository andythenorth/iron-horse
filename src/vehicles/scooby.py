from train import MailEngineRailcarConsist, DieselRailcarUnit

consist = MailEngineRailcarConsist(id='scooby',
                                   base_numeric_id=3070,
                                   name='Scooby',
                                   role='mail_railcar',
                                   power=420,
                                   type_base_running_cost_points=-32,  # dibble running costs for game balance
                                   gen=4,
                                   sprites_complete=True,
                                   intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 chassis='railcar')
