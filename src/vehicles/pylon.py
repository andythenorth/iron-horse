from train import MailEngineRailcarConsist, ElectricRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='pylon',
                                       base_numeric_id=2120,
                                       name='Pylon',
                                       role='mail_railcar_2',
                                       power=1000,
                                       pantograph_type='z-shaped-single-with-base',
                                       easter_egg_haulage_speed_bonus=True,
                                       gen=6,
                                       sprites_complete=True,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarMailUnit,
                     weight=45,
                     vehicle_length=8,
                     chassis='railcar')

    return consist
