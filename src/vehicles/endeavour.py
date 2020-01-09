from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='endeavour',
                            base_numeric_id=4250,
                            name='Endeavour',
                            role='heavy_freight_3',
                            power=4700,
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            intro_date_offset=3,  # let's be a little bit later for this one
                            gen=6,
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=125,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
