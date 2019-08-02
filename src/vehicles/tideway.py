from train import MailEngineMetroConsist, MetroUnit


def main(roster):
    consist = MailEngineMetroConsist(roster=roster,
                                     id='tideway',
                                     base_numeric_id=2200,
                                     name='Tideway',
                                     role='mail_metro',
                                     power=1100,
                                     gen=3,
                                     sprites_complete=True)

    consist.add_unit(type=MetroUnit,
                     weight=32,
                     # set capacity for freight; mail will be automatically calculated
                     capacity=30,
                     chassis='railcar_32px',
                     tail_light='metro_32px_1',
                     repeat=2)

    return consist
