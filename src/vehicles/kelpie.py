from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='kelpie',
                            base_numeric_id=900,
                            name='Kelpie',
                            role='express',
                            role_child_branch_num=1,
                            power=1450,
                            random_reverse=True,
                            intro_date_offset=-2,  # let's not have everything turn up in 1960
                            gen=4,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=72,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
