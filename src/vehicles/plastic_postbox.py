from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='plastic_postbox',
                                       base_numeric_id=3080,
                                       name='Plastic Postbox',
                                       role='mail_railcar_1',
                                       power=560,
                                       gen=5,
                                       sprites_complete=True,
                                       intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=37,
                     chassis='railcar_32px')

    return consist
