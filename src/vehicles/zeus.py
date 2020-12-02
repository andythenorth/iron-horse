from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='zeus',
                                            base_numeric_id=3210,
                                            name='Zeus',
                                            role='pax_railcar',
                                            role_child_branch_num=2,
                                            power=620,
                                            pantograph_type='z-shaped-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=6,
                                            sprites_complete=True,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarPaxUnit,
                     weight=39,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    consist.description = """Gets you from A to Z and back."""
    consist.foamer_facts = """BR Class 365 <i>Networker Express</i>"""

    return consist
