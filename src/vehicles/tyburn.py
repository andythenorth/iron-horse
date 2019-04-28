from train import MailEngineMetroConsist, MetroUnit


def main(roster):
    consist = MailEngineMetroConsist(roster=roster,
                                     id='tyburn',
                                     base_numeric_id=2190,
                                     name='Tyburn',
                                     role='mail_metro',
                                     power=900,
                                     gen=2,
                                     sprites_complete=True)

    consist.add_unit(type=MetroUnit,
                     weight=32,
                     vehicle_length=8,
                     # set capacity for freight; mail will be automatically calculated
                     capacity=27,
                     chassis='railcar_32px',
                     repeat=2)

    return consist
