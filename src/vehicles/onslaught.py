from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='onslaught',
                            base_numeric_id=4290,
                            name='Onslaught',
                            role='heavy_express_3',
                            power=3300,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=-7, # let's be really early with this one to give a mail engine matching Blaze HST intro date
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=100,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
