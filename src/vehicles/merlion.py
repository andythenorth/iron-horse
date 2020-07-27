from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='merlion',
                            base_numeric_id=4920,
                            name='Merlion',
                            role='freight',
                            role_child_branch_num=-2,
                            power=1750,
                            tractive_effort_coefficient=0.26,
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=-2,  # let's be a littler earlier for this one
                            cc_liveries=[['COLOUR_GREY']],
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=105,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
