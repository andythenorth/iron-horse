from train import SlidingWallCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # starts gen 4, B and C only

    consist = SlidingWallCarConsist(roster_id='pony',
                            base_numeric_id=1570,
                            gen=4,
                            subtype='B',
                            intro_date_offset=5,  # let's be a little bit later for this one
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')


    consist = SlidingWallCarConsist(roster_id='pony',
                            base_numeric_id=1790,
                            gen=4,
                            subtype='C',
                            intro_date_offset=5,  # let's be a little bit later for this one
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='4_axle_1cc_filled_32px')


    consist = SlidingWallCarConsist(roster_id='pony',
                            base_numeric_id=410,
                            gen=5,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='2_axle_1cc_filled_24px')


    consist = SlidingWallCarConsist(roster_id='pony',
                            base_numeric_id=440,
                            gen=5,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='4_axle_1cc_filled_32px')


    consist = SlidingWallCarConsist(roster_id='pony',
                            base_numeric_id=5190,
                            gen=5,
                            subtype='D',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='2_axle_1cc_filled_20px',
                     symmetry_type='asymmetric',
                     spriterow_num=0)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='2_axle_1cc_filled_20px',
                     symmetry_type='asymmetric',
                     spriterow_num=2)


    consist = SlidingWallCarConsist(roster_id='pony',
                            base_numeric_id=330,
                            gen=6,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='2_axle_1cc_filled_24px')


    consist = SlidingWallCarConsist(roster_id='pony',
                            base_numeric_id=320,
                            gen=6,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='4_axle_1cc_filled_32px')


    consist = SlidingWallCarConsist(roster_id='pony',
                            base_numeric_id=5200,
                            gen=6,
                            subtype='D',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='2_axle_1cc_filled_20px',
                     symmetry_type='asymmetric',
                     spriterow_num=0)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='2_axle_1cc_filled_20px',
                     symmetry_type='asymmetric',
                     spriterow_num=2)


