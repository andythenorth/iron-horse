from train import MailEngineRailcarConsist, DieselRailcarUnit

consist = MailEngineRailcarConsist(id='gowsty',
                                   base_numeric_id=1760,
                                   name='Gowsty',
                                   role='mail_railcar',
                                   power=280,
                                   gen=3,
                                   sprites_complete=True,
                                   intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=30,
                 vehicle_length=8,
                 capacity=30,
                 chassis='railcar')
