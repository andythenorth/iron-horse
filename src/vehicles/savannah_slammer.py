from train import EngineConsist, DieselEngineUnit

def main():    
    consist = EngineConsist(id='savannah_slammer',
                            base_numeric_id=1540,
                            name='Savannah Slammer',
                            power=500,
                            intro_date=1980)
    
    consist.add_unit(type=DieselEngineUnit,
                     weight=65,
                     vehicle_length=8,
                     capacity=65,
                     spriterow_num=0)

    return consist