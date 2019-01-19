from train import MailEngineRailcarConsist, ElectricRailcarBaseUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='jupiter',
                                       base_numeric_id=3190,
                                       name='Jupiter',
                                       role='mail_railcar',
                                       power=850,
                                       pantograph_type='z-shaped-single',
                                       easter_egg_haulage_speed_bonus=True,
                                       gen=5,
                                       sprites_complete=False,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarBaseUnit,
                     weight=45,
                     vehicle_length=8,
                     # set capacity for freight; mail will be automatically calculated; match to 8/8 mail car for this gen
                     capacity=24,
                     chassis='railcar')

    return consist
