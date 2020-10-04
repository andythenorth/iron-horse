from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='geronimo',
                                            base_numeric_id=2140,
                                            name='Geronimo',
                                            role='pax_railcar',
                                            role_child_branch_num=2,
                                            power=420,  # RL EMU HP is much lower per single car, but eh
                                            pantograph_type='z-shaped-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=4,
                                            sprites_complete=True,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarPaxUnit,
                     weight=35,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    consist.description = """More Speed. More Comfort. More Trains."""
    consist.foamer_facts = """BR 2-HAP, 4EPB, Class 302."""

    return consist
