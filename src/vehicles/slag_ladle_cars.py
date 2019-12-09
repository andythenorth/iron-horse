from train import SlagLadleCarConsist, SlagLadleCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = SlagLadleCarConsist(roster_id='pony',
                                  base_numeric_id=4030,
                                  gen=1,
                                  subtype='U',
                                  speed=35, # note rare non-standard speed, don't spill molten slag eh?
                                  suppress_animated_pixel_warnings=True)

    consist.add_unit(type=SlagLadleCar,
                     chassis='buffers_only_16px')


    consist = SlagLadleCarConsist(roster_id='pony',
                                  base_numeric_id=4040,
                                  gen=4,
                                  subtype='U',
                                  speed=45, # note rare non-standard speed, don't spill molten slag eh?
                                  suppress_animated_pixel_warnings=True)

    consist.add_unit(type=SlagLadleCar,
                     chassis='buffers_only_16px')
