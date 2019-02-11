from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='breeze',
                                            base_numeric_id=3200,
                                            name='Breeze',
                                            role='pax_railcar_2',
                                            power=650,  # RL EMU HP is much lower, but eh
                                            pantograph_type='z-shaped-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=5,
                                            sprites_complete=False,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarPaxUnit,
                     weight=42,
                     vehicle_length=8,
                     chassis='railcar')

    return consist
