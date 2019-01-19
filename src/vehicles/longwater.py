from train import MailEngineMetroConsist, MetroUnit

def main():    
    consist = MailEngineMetroConsist(id='longwater',
                                     base_numeric_id=290,
                                     name='Longwater',
                                     role='mail_metro',
                                     power=600,
                                     gen=1,
                                     sprites_complete=True)
    
    consist.add_unit(type=MetroUnit,
                     weight=32,
                     vehicle_length=8,
                     # set capacity for freight; mail will be automatically calculated
                     capacity=24,
                     chassis='railcar',
                     repeat=2)

    return consist