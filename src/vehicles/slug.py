from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='slug',
                            base_numeric_id=1000,
                            name='Slug',
                            role='freight',
                            role_child_branch_num=1,
                            power=1950, # progression calculated to maintain hp/speed ratio from previous gen
                            random_reverse=True,
                            gen=5,
                            cc_liveries=[['COLOUR_WHITE', 'COLOUR_BROWN'], ['COLOUR_PINK']],
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
