from train import VehicleParsBoxCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # starts gen 4, B and C only

    consist = VehicleParsBoxCarConsist(roster_id='pony',
                            base_numeric_id=4620,
                            gen=4,
                            subtype='B',
                            intro_date_offset=3,  # let's be a little bit later for this one
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')


    consist = VehicleParsBoxCarConsist(roster_id='pony',
                            base_numeric_id=4630,
                            gen=4,
                            subtype='C',
                            intro_date_offset=3,  # let's be a little bit later for this one
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='4_axle_1cc_filled_32px')


    consist = VehicleParsBoxCarConsist(roster_id='pony',
                            base_numeric_id=4640,
                            gen=5,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='2_axle_1cc_filled_24px')


    consist = VehicleParsBoxCarConsist(roster_id='pony',
                            base_numeric_id=4650,
                            gen=5,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='4_axle_1cc_filled_32px')


    consist = VehicleParsBoxCarConsist(roster_id='pony',
                            base_numeric_id=4660,
                            gen=6,
                            subtype='B',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='2_axle_1cc_filled_24px')


    consist = VehicleParsBoxCarConsist(roster_id='pony',
                            base_numeric_id=4670,
                            gen=6,
                            subtype='C',
                            sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     suppress_roof_sprite=True, # non-standard roof for this wagon
                     chassis='4_axle_1cc_filled_32px')
