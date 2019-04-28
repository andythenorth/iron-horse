from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='workish',
                                       base_numeric_id=260,
                                       name='Workish',
                                       role='mail_railcar_1',
                                       base_track_type='NG',
                                       power=360,
                                       gen=3,
                                       sprites_complete=True)

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=18,
                     vehicle_length=6,
                     chassis='railcar_ng_24px')

    return consist
