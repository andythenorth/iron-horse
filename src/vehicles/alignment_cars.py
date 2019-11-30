from train import AlignmentCarConsist, AlignmentCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = AlignmentCarConsist(roster_id='pony',
                                base_numeric_id=20,
                                gen=1,
                                subtype='A',
                                sprites_complete=False)

    consist.add_unit(type=AlignmentCar,
                     vehicle_length=4,
                     chassis='2_axle_solid_express_16px')


    consist = AlignmentCarConsist(roster_id='pony',
                                base_numeric_id=30,
                                gen=1,
                                subtype='B',
                                sprites_complete=False)

    consist.add_unit(type=AlignmentCar,
                     vehicle_length=6,
                     chassis='4_axle_solid_express_24px')


    consist = AlignmentCarConsist(roster_id='pony',
                                base_numeric_id=40,
                                gen=1,
                                subtype='C',
                                sprites_complete=False)

    consist.add_unit(type=AlignmentCar,
                     vehicle_length=8,
                     chassis='4_axle_solid_express_32px')
