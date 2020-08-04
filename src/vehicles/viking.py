from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='viking',
                            base_numeric_id=780,
                            name='Viking',
                            role='freight',
                            role_child_branch_num=-2,
                            power=1950,
                            random_reverse=True,
                            gen=5,
                            intro_date_offset=6, # introduce later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=74,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
