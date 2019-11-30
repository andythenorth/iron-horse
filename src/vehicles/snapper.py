from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
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
                     effect_z_offset=11, # reduce smoke z position to suit NG engine height
                     chassis='railcar_ng_24px',
                     tail_light='railcar_24px_1')

    return consist
