from train import CabooseCarConsist, CabooseCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = CabooseCarConsist(roster='pony',
                                base_numeric_id=1290,
                                gen=1,
                                subtype='A',
                                track_type='NG')

    consist.add_unit(type=CabooseCar,
                     vehicle_length=4,
                     chassis='2_axle_caboose_16px')


    #--------------- pony ----------------------------------------------------------------------
    consist = CabooseCarConsist(roster='pony',
                                base_numeric_id=1280,
                                gen=1,
                                subtype='A',
                                sprites_complete=True)

    consist.add_unit(type=CabooseCar,
                     vehicle_length=4,
                     chassis='2_axle_caboose_16px')


    consist = CabooseCarConsist(roster='pony',
                                base_numeric_id=2210,
                                gen=1,
                                subtype='B',
                                sprites_complete=True)

    consist.add_unit(type=CabooseCar,
                     vehicle_length=6,
                     chassis='4_axle_caboose_24px')