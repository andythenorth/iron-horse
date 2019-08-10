from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='zorro',
                                       base_numeric_id=310,
                                       name='Zorro',
                                       role='mail_railcar_1',
                                       base_track_type='NG',
                                       power=500,
                                       gen=4,
                                       sprites_complete=True)

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=18,
                     effect_z_offset=11, # reduce smoke z position to suit NG engine height
                     chassis='railcar_ng_24px',
                     tail_light='railcar_24px_1')

    return consist
