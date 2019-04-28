from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='mumble',
                                            base_numeric_id=140,
                                            name='Mumble',
                                            role='pax_railcar_1',
                                            base_track_type='NG',
                                            power=250,
                                            gen=3,
                                            sprites_complete=True)

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=18,
                     vehicle_length=6,
                     chassis='railcar_ng_24px')

    return consist
