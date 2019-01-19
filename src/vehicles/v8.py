from train import EngineConsist, ElectricEngineUnit

def main():    
    consist = EngineConsist(id='v8',
                            base_numeric_id=410,
                            name='V8 2-C+C-2',
                            power=4000,
                            intro_date=1949)
    
    consist.add_unit(type=ElectricEngineUnit,
                     weight=160,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist