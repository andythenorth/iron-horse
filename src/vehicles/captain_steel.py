from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='captain_steel',
                            base_numeric_id=4990,
                            name='Captain Steel',
                            role='branch_freight',
                            role_child_branch_num=-1,
                            power=1150,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=-6,
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=70,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.description = """"""
    consist.foamer_facts = """Alco s1, EMD SW1200, Brush Bagnall,"""

    return consist
