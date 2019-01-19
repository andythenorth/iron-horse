from train import MailEngineRailcarConsist, ElectricRailcarUnit


def main(roster):
    consist = MailEngineRailcarConsist(roster=roster,
                                       id='dover',
                                       base_numeric_id=700,
                                       name='Dover',
                                       role='mail_railcar',
                                       power=700,
                                       pantograph_type='z-shaped-single',
                                       easter_egg_haulage_speed_bonus=True,
                                       gen=4,
                                       sprites_complete=False,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarUnit,
                     weight=45,
                     vehicle_length=8,
                     # set capacity for freight; mail will be automatically calculated; match to 8/8 mail car for this gen
                     capacity=22,
                     chassis='railcar')

    return consist
