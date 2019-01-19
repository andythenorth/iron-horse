from train import MailEngineRailcarConsist, DieselRailcarBaseUnit

def main():    
    consist = MailEngineRailcarConsist(id='mail_rail',
                                       base_numeric_id=3000,
                                       name='Mail Rail',
                                       role='mail_railcar',
                                       power=700,
                                       gen=6,
                                       sprites_complete=True,
                                       intro_date_offset=-5)  # introduce early by design
    
    consist.add_unit(type=DieselRailcarBaseUnit,
                     weight=37,
                     vehicle_length=8,
                     # set capacity for freight; mail will be automatically calculated; match to 8/8 mail car for this gen
                     capacity=24,
                     chassis='railcar')

    return consist