from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='scooby',
                                       base_numeric_id=3070,
                                       name='Scooby',
                                       role='mail_railcar_1',
                                       power=420,
                                       gen=4,
                                       sprites_complete=True,
                                       intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=37,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    return consist
