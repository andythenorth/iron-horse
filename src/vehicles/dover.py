from train import MailEngineRailcarConsist, ElectricRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='dover',
                                       base_numeric_id=700,
                                       name='Dover',
                                       role='mail_railcar_2',
                                       power=700,
                                       pantograph_type='z-shaped-single-with-base',
                                       easter_egg_haulage_speed_bonus=True,
                                       gen=4,
                                       sprites_complete=True,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarMailUnit,
                     weight=44,
                     vehicle_length=8,
                     chassis='railcar')

    return consist
