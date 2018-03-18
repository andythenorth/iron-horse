from train import LivestockCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=1030,
                                  gen=1,
                                  subtype='A',
                                  track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    
    #--------------- pony ----------------------------------------------------------------------
    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=1010,
                                  gen=1,
                                  subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    
    # no gen 2 needed

    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=2680,
                                  gen=3,
                                  subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    
    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=1020,
                                  gen=4,
                                  subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    
    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=2720,
                                  gen=5,
                                  subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    
    consist = LivestockCarConsist(roster='pony',
                                  base_numeric_id=2710,
                                  gen=6,
                                  subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    
    #--------------- llama ----------------------------------------------------------------------

    consist = LivestockCarConsist(roster='llama',
                                  base_numeric_id=1040,
                                  gen=1,
                                  subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    
    consist = LivestockCarConsist(roster='llama',
                                  base_numeric_id=1430,
                                  gen=2,
                                  subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    
    consist = LivestockCarConsist(roster='llama',
                                  base_numeric_id=1050,
                                  gen=1,
                                  subtype='A',
                                  track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    
    consist = LivestockCarConsist(roster='llama',
                                  base_numeric_id=1520,
                                  gen=2,
                                  subtype='A',
                                  track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    
    #--------------- antelope ----------------------------------------------------------------------
    consist = LivestockCarConsist(roster='antelope',
                                  base_numeric_id=1720,
                                  gen=1,
                                  subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    
    consist = LivestockCarConsist(roster='antelope',
                                  base_numeric_id=2150,
                                  gen=1,
                                  subtype='A',
                                  track_type='NG')

    consist.add_unit(type=FreightCar,
                     vehicle_length=5)

    