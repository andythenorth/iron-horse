from train import MailEngineMetroConsist, MetroUnit


def main(roster_id):
    consist = MailEngineMetroConsist(roster_id=roster_id,
                                     id='tideway',
                                     base_numeric_id=2200,
                                     name='Tideway',
                                     role='mail_metro',
                                     role_child_branch_num=1,
                                     power=1100,
                                     gen=3,
                                     default_livery_extra_docs_examples=[('COLOUR_RED', 'COLOUR_BLUE')],
                                     sprites_complete=True)

    consist.add_unit(type=MetroUnit,
                     weight=32,
                     # set capacity for freight; mail will be automatically calculated
                     capacity=30,
                     chassis='railcar_32px',
                     tail_light='metro_32px_1',
                     repeat=2)

    consist.description = """Hate to stand out in the crowd, whispering occasionally.""" # B-Movie
    consist.foamer_facts = """London Underground 1996 Stock."""

    return consist
