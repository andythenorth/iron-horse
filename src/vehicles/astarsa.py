from train import EngineConsist, DieselEngineUnit

def main():    # for rest of stats, look up EMD G22CW
    consist = EngineConsist(id='astarsa',
                            base_numeric_id=50,
                            name='Astarsa',
                            power=1600,
                            intro_date=1969)
    
    consist.add_unit(type=DieselEngineUnit,
                     weight=40,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist