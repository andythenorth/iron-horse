from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='growler',
                            base_numeric_id=2240,
                            name='Growler',
                            role='freight',
                            role_child_branch_num=1,
                            power=1750,
                            random_reverse=True,
                            gen=4,
                            cc_liveries=[['COLOUR_GREY']],
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=100,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
