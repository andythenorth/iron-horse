from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='slug',
                            base_numeric_id=1000,
                            name='Slug',
                            role='freight_1',
                            power=1900, # progression calculated to maintain hp/speed ratio from previous gen
                            random_reverse=True,
                            gen=5,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
