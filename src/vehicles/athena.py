from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='athena',
                                            base_numeric_id=2150,
                                            name='Athena',
                                            role='pax_railcar_2',
                                            power=350,  # RL EMU HP is much lower, but eh
                                            pantograph_type='diamond-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=3,
                                            sprites_complete=True,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarPaxUnit,
                     weight=32,
                     vehicle_length=8,
                     chassis='railcar_32px')

    return consist
