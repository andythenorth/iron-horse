from train import MailEngineRailcarConsist, ElectricRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(roster_id=roster_id,
                                       id='dover',
                                       base_numeric_id=700,
                                       name='Dover',
                                       role='mail_railcar_2',
                                       power=540,
                                       pantograph_type='z-shaped-single-with-base',
                                       easter_egg_haulage_speed_bonus=True,
                                       use_3_unit_sets=True,
                                       gen=4,
                                       sprites_complete=True,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarMailUnit,
                     weight=39,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    return consist
