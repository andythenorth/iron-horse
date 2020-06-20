from train import VehicleTransporterCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = VehicleTransporterCarConsist(roster_id='pony',
                                           base_numeric_id=4680,
                                           gen=5,
                                           subtype='B')

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_greebled_24px')


    consist = VehicleTransporterCarConsist(roster_id='pony',
                                           base_numeric_id=4690,
                                           gen=5,
                                           subtype='C')

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')
