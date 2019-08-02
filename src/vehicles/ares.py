from train import MailEngineRailcarConsist, ElectricRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='ares',
                                       base_numeric_id=2130,
                                       name='Ares',
                                       role='mail_railcar_2',
                                       power=550,
                                       pantograph_type='diamond-single-with-base',
                                       easter_egg_haulage_speed_bonus=True,
                                       gen=3,
                                       sprites_complete=True,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarMailUnit,
                     weight=32,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_1')

    return consist
