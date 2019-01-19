from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='gowsty',
                                       base_numeric_id=1760,
                                       name='Gowsty',
                                       role='mail_railcar_1',
                                       power=280,
                                       gen=3,
                                       sprites_complete=True,
                                       intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=30,
                     vehicle_length=8,
                     chassis='railcar')

    return consist
