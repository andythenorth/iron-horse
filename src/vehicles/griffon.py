from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='griffon',
                            base_numeric_id=2840,
                            name='Griffon',
                            role='express',
                            role_child_branch_num=1,
                            power=1550,
                            random_reverse=True,
                            gen=5,
                            alternative_cc_livery='RAILFREIGHT_TRIPLE_GREY',
                            default_livery_extra_docs_examples=[('COLOUR_GREY', 'COLOUR_YELLOW'), ('COLOUR_WHITE', 'COLOUR_GREY'), ('COLOUR_GREY', 'COLOUR_GREY'), ('COLOUR_LIGHT_BLUE', 'COLOUR_WHITE')],
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=74,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.foamer_facts = """BR Class 33."""

    return consist
