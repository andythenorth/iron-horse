from train import VehicleTransporterCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = VehicleTransporterCarConsist(roster='pony',
                                           base_numeric_id=1530,
                                           gen=3,
                                           subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)
