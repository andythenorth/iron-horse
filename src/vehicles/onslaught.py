from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='onslaught',
                            base_numeric_id=4290,
                            name='Onslaught',
                            role='freight_2',
                            power=2400,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=-4, # let's be a little early with this one
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
