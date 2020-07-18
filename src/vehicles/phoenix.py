from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='phoenix',
                            base_numeric_id=160,
                            name='Phoenix',
                            role='freight',
                            role_child_branch_num=1,
                            power=2150, # progression calculated to maintain hp/speed ratio from previous gen
                            random_reverse=True,
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=120,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
