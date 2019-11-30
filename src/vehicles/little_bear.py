from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='little_bear',
                            base_numeric_id=1730,
                            name='Little Bear',
                            role='branch_freight',
                            power=1150,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=-6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=68,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
