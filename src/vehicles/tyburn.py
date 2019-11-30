from train import MailEngineMetroConsist, MetroUnit


def main(roster_id):
    consist = MailEngineMetroConsist(roster_id=roster_id,
                                     id='tyburn',
                                     base_numeric_id=2190,
                                     name='Tyburn',
                                     role='mail_metro',
                                     power=900,
                                     gen=2,
                                     sprites_complete=True)

    consist.add_unit(type=MetroUnit,
                     weight=32,
                     # set capacity for freight; mail will be automatically calculated
                     capacity=27,
                     chassis='railcar_32px',
                     tail_light='metro_32px_1',
                     repeat=2)

    return consist
