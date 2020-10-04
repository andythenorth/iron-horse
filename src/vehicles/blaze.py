from train import PassengerHSTCabEngineConsist, DieselEngineUnit


def main(roster_id):
    consist = PassengerHSTCabEngineConsist(roster_id=roster_id,
                                           id='blaze',
                                           base_numeric_id=3330,
                                           name='Blaze HST',
                                           role='hst', # quite a specific role, may or may not scale to other rosters
                                           role_child_branch_num=1,
                                           power=5000,
                                           intro_date_offset=-10,  # let's be a little bit earlier for this one - keep coaches matched
                                           gen=5,
                                           sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=70,
                     vehicle_length=8,
                     effect_offsets=[(0, 1), (0, -1)], # double the smoke eh?
                     spriterow_num=0,
                     tail_light='hst_32px_1')

    consist.description = """She was like a bird for speed, an arrow for directness."""
    consist.foamer_facts = """BR Class 43 (High Speed Train)."""

    return consist
