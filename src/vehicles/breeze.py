from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='breeze',
                                            base_numeric_id=3200,
                                            name='Breeze',
                                            role='pax_railcar',
                                            role_child_branch_num=2,
                                            power=520,
                                            pantograph_type='z-shaped-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=5,
                                            sprites_complete=True,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarPaxUnit,
                     weight=38,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    consist.description = """"""
    consist.cite = """Arabella Unit"""
    consist.foamer_facts = """BR Class 319, Class 455."""

    return consist
