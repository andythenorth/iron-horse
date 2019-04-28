from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='mail_rail',
                                       base_numeric_id=3000,
                                       name='Mail Rail',
                                       role='mail_railcar_1',
                                       power=700,
                                       gen=6,
                                       sprites_complete=True,
                                       intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=37,
                     vehicle_length=8,
                     chassis='railcar_32px')

    return consist
