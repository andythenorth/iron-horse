from train import SiloCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SiloCarConsist(roster='pony',
                             base_numeric_id=2860,
                             gen=5,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_32px')


    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
