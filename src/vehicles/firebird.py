from train import PassengerHSTCabEngineConsist, DieselEngineUnit


def main(roster_id):
    consist = PassengerHSTCabEngineConsist(roster_id=roster_id,
                                           id='firebird',
                                           base_numeric_id=3830,
                                           name='Firebird',
                                           role='hst', # quite a specific role, may or may not scale to other rosters
                                           power=3300, # it's the Deltic that never was!
                                           gen=4,
                                           sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=65,
                     vehicle_length=8,
                     capacity=16,
                     effect_offsets=[(0, 1), (0, -1)], # double the smoke eh?
                     spriterow_num=0,
                     tail_light='hst_32px_1')

    return consist
