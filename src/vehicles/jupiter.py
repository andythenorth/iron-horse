from train import MailEngineRailcarConsist, ElectricRailcarMailUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='jupiter',
                                       base_numeric_id=3190,
                                       name='Jupiter',
                                       role='mail_railcar_2',
                                       power=850,
                                       pantograph_type='z-shaped-single',
                                       easter_egg_haulage_speed_bonus=True,
                                       gen=5,
                                       sprites_complete=False,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarMailUnit,
                     weight=45,
                     vehicle_length=8,
                     chassis='railcar')

    return consist
