from train import PassengerEngineRailcarConsist, DieselRailcarBaseUnit

def main():    
    consist = PassengerEngineRailcarConsist(id='snapper',
                                            base_numeric_id=590,
                                            name='Snapper',
                                            role='pax_railcar',
                                            base_track_type='NG',
                                            power=350,
                                            gen=4,
                                            sprites_complete=True)
    
    consist.add_unit(type=DieselRailcarBaseUnit,
                     weight=18,
                     vehicle_length=6,
                     capacity=30,
                     chassis='railcar_ng')

    return consist