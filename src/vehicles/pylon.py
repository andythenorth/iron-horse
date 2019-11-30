from train import MailEngineRailcarConsist, ElectroDieselRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(roster_id=roster_id,
                                       id='pylon',
                                       base_numeric_id=2120,
                                       name='Pylon',
                                       role='mail_railcar_2',
                                       power=1000,
                                       power_by_railtype={'RAIL': 450, 'ELRL': 1000}, # bit nerfed on diesel, by design
                                       pantograph_type='z-shaped-single-with-base',
                                       easter_egg_haulage_speed_bonus=True,
                                       gen=6,
                                       sprites_complete=True,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectroDieselRailcarMailUnit,
                     weight=44,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    return consist
