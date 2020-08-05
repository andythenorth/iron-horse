from train import MailEngineRailcarConsist, ElectroDieselRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(roster_id=roster_id,
                                       id='pylon',
                                       base_numeric_id=2120,
                                       name='Pylon',
                                       role='mail_railcar',
                                       role_child_branch_num=2,
                                       power=820,
                                       power_by_railtype={'RAIL': 450, 'ELRL': 820}, # bit nerfed on diesel, by design
                                       pantograph_type='z-shaped-single-with-base',
                                       easter_egg_haulage_speed_bonus=True,
                                       use_3_unit_sets=True,
                                       gen=6,
                                       sprites_complete=True,
                                       intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectroDieselRailcarMailUnit,
                     weight=37, # higher weight than previous gen as bi-mode
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    consist.foamer_facts = """BR Class 325."""

    return consist
