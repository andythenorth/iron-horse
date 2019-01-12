from train import MailEngineRailcarConsist, ElectricRailcarUnit

consist = MailEngineRailcarConsist(id='breeze',
                                   base_numeric_id=3190,
                                   name='Breeze',
                                   role='mail_railcar',
                                   power=850,
                                   pantograph_type='z-shaped-single',
                                   gen=5,
                                   sprites_complete=False,
                                   intro_date_offset=-3)  # introduce early by design

consist.add_unit(type=ElectricRailcarUnit,
                 weight=45,
                 vehicle_length=8,
                 # set capacity for freight; mail will be automatically calculated; match to 8/8 mail car for this gen
                 capacity=24,
                 chassis='railcar')
