from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='cheddar_valley',
                            base_numeric_id=220,
                            name='Cheddar Valley',
                            role='heavy_freight_3',
                            power=4000,
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            intro_date_offset=5,  # let's be a little bit later for this one
                            gen=5,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=125,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
