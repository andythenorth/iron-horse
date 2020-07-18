from train import MailEngineMetroConsist, MetroUnit


def main(roster_id):
    consist = MailEngineMetroConsist(roster_id=roster_id,
                                     id='longwater',
                                     base_numeric_id=290,
                                     name='Longwater',
                                     role='mail_metro',
                                     role_child_branch_num=1,
                                     power=600,
                                     gen=1,
                                     sprites_complete=True)

    consist.add_unit(type=MetroUnit,
                     weight=32,
                     # set capacity for freight; mail will be automatically calculated
                     capacity=24,
                     chassis='railcar_32px',
                     tail_light='metro_32px_1',
                     repeat=2)

    return consist
