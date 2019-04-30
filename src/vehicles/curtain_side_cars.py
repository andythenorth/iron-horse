from train import CurtainSideCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # gen 5 start, only B and C lengths

    consist = CurtainSideCarConsist(roster='pony',
                            base_numeric_id=340,
                            gen=5,
                            subtype='B',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_24px')

    consist = CurtainSideCarConsist(roster='pony',
                            base_numeric_id=350,
                            gen=5,
                            subtype='C',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_32px')

    consist = CurtainSideCarConsist(roster='pony',
                            base_numeric_id=370,
                            gen=6,
                            subtype='B',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_24px')

    consist = CurtainSideCarConsist(roster='pony',
                            base_numeric_id=400,
                            gen=6,
                            subtype='C',
                            sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
