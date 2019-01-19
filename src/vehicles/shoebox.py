from train import EngineConsist, ElectroDieselEngineUnit

def main():    
    consist = EngineConsist(id='shoebox',
                            base_numeric_id=280,
                            name='Shoebox',
                            role='branch_express',
                            power=950,
                            power_by_railtype={'RAIL': 950, 'ELRL': 1800},
                            random_reverse=True,
                            pantograph_type='z-shaped-single',
                            gen=4,
                            sprites_complete=True)
    
    consist.add_unit(type=ElectroDieselEngineUnit,
                     weight=65,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist