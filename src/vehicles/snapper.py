from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='snapper',
                                            base_numeric_id=590,
                                            name='Snapper',
                                            role='pax_railcar_1',
                                            base_track_type='NG',
                                            power=350,
                                            gen=4,
                                            sprites_complete=True)

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=18,
                     vehicle_length=6,
                     chassis='railcar_ng_24px')

    return consist
