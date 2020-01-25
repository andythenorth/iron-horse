from train import SlagLadleCarConsist, SlagLadleCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------

    consist = SlagLadleCarConsist(roster_id='pony',
                                  base_numeric_id=4440,
                                  gen=1,
                                  subtype='U',
                                  base_track_type='NG',
                                  speed=35, # note rare non-standard speed, don't spill molten slag eh?
                                  sprites_complete=False)

    consist.add_unit(type=SlagLadleCar,
                     chassis='buffers_only_16px')

    #--------------- pony ----------------------------------------------------------------------

    consist = SlagLadleCarConsist(roster_id='pony',
                                  base_numeric_id=4030,
                                  gen=1,
                                  subtype='U',
                                  speed=35, # note rare non-standard speed, don't spill molten slag eh?
                                  sprites_complete=True)

    consist.add_unit(type=SlagLadleCar,
                     chassis='buffers_only_16px')


    consist = SlagLadleCarConsist(roster_id='pony',
                                  base_numeric_id=4040,
                                  gen=4,
                                  subtype='U',
                                  speed=35, # note rare non-standard speed, don't spill molten slag eh?
                                  sprites_complete=True)

    consist.add_unit(type=SlagLadleCar,
                     chassis='buffers_only_16px')
