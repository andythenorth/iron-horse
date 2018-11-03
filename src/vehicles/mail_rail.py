from train import MailEngineRailcarConsist, DieselRailcarUnit

consist = MailEngineRailcarConsist(id='mail_rail',
                                   base_numeric_id=3000,
                                   name='Mail Rail',
                                   role='mail_railcar',
                                   power=700,
                                   gen=6,
                                   sprites_complete=True,
                                   intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 chassis='railcar')
