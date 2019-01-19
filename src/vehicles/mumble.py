from train import PassengerEngineRailcarConsist, DieselRailcarBaseUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='mumble',
                                            base_numeric_id=140,
                                            name='Mumble',
                                            role='pax_railcar',
                                            base_track_type='NG',
                                            power=250,
                                            gen=3,
                                            sprites_complete=True)

    consist.add_unit(type=DieselRailcarBaseUnit,
                     weight=18,
                     vehicle_length=6,
                     capacity=30,
                     chassis='railcar_ng')

    return consist
