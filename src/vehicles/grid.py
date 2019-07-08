from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='grid',
                            base_numeric_id=3350,
                            name='Grid',
                            role='heavy_freight_1',
                            power=3300,
                            joker=True,  # this engine doesn't fit the intro date pattern  by design
                            random_reverse=True,
                            intro_date_offset=-7,  # let's be a little bit earlier for this one
                            gen=5,
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
