from train import IngotCarConsist, IngotCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------

    consist = IngotCarConsist(roster_id='pony',
                                  base_numeric_id=5150,
                                  gen=1,
                                  subtype='U',
                                  base_track_type='NG',
                                  speed=35, # note rare non-standard speed, don't spill hot ingots eh?
                                  sprites_complete=False)

    consist.add_unit(type=IngotCar,
                     chassis='buffers_only_16px')
