from train import MailEngineRailcarConsist, DieselRailcarBaseUnit

consist = MailEngineRailcarConsist(id='plastic_postbox',
                                   base_numeric_id=3080,
                                   name='Plastic Postbox',
                                   role='mail_railcar',
                                   power=560,
                                   gen=5,
                                   sprites_complete=True,
                                   intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=DieselRailcarBaseUnit,
                 weight=37,
                 vehicle_length=8,
                 # set capacity for freight; mail will be automatically calculated; match to 8/8 mail car for this gen
                 capacity=24,
                 chassis='railcar')
