from train import PassengerEngineRailcarConsist, ElectroDieselRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='zeus',
                                            base_numeric_id=3210,
                                            name='Zeus',
                                            role='pax_railcar_2',
                                            power=800,  # RL EMU HP is much lower, but eh
                                            power_by_railtype={'RAIL': 360, 'ELRL': 800},
                                            pantograph_type='z-shaped-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=6,
                                            sprites_complete=True,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectroDieselRailcarPaxUnit,
                     weight=47,
                     vehicle_length=8,
                     chassis='railcar')

    return consist
