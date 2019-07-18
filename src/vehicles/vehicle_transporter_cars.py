from train import VehicleTransporterCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = VehicleTransporterCarConsist(roster='pony',
                                           base_numeric_id=3570,
                                           gen=5,
                                           subtype='C')

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_32px')
