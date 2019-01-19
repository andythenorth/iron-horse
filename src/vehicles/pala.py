from train import EngineConsist, DieselEngineUnit

def main():    # standard gauge GE Shovelnose
    consist = EngineConsist(id='pala',
                            base_numeric_id=320,
                            name='Pala',
                            power=1200,
                            intro_date=1955)
    
    consist.add_unit(type=DieselEngineUnit,
                     weight=105,
                     vehicle_length=7,
                     spriterow_num=0)

    return consist