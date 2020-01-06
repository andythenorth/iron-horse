from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='grid',
                            base_numeric_id=3350,
                            name='Grid',
                            role='heavy_freight_1',
                            power=3300, # drops a bit on hp/speed from previous gen, but engine weight is lower
                            random_reverse=True,
                            intro_date_offset=-7,  # let's be a little bit earlier for this one
                            gen=5,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
