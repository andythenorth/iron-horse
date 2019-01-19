from train import PassengerEngineRailcarConsist, ElectricRailcarUnit

def main():    
    consist = PassengerEngineRailcarConsist(id='geronimo',
                                            base_numeric_id=2140,
                                            name='Geronimo',
                                            role='pax_railcar',
                                            power=500,  # RL EMU HP is much lower, but eh
                                            pantograph_type='z-shaped-single',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=4,
                                            sprites_complete=False,
                                            intro_date_offset=-3)  # introduce early by design
    
    consist.add_unit(type=ElectricRailcarUnit,
                     weight=40,
                     vehicle_length=8,
                     capacity=40,
                     chassis='railcar')

    return consist