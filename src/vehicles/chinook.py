from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='chinook',
                            base_numeric_id=120,
                            name='Chinook',
                            role='heavy_freight',
                            role_child_branch_num=1,
                            power=2900,
                            gen=4,
                            alternative_cc_livery='RAILFREIGHT_RED_STRIPE',
                            default_livery_extra_docs_examples=[('COLOUR_PALE_GREEN', 'COLOUR_GREY'), ('COLOUR_BLUE', 'COLOUR_GREY')],
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=80,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=DieselEngineUnit,
                     weight=80,
                     vehicle_length=6,
                     spriterow_num=1)

    consist.description = """I send these out in twos."""
    consist.cite = """Mr. Train"""


    return consist
