from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='hercules',
                            base_numeric_id=1720,
                            name='Hercules',
                            role='branch_freight',
                            power=1300,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=2, # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=71,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
