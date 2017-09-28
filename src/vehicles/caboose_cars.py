import global_constants
from train import CabooseConsistShort, CabooseConsistLong, FreightCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CabooseConsistShort(title = '[Caboose Car] Short',
                             roster = 'pony',
                             base_numeric_id = 1280,
                             vehicle_generation = 1,
                                            speedy = True)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 0,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    consist = CabooseConsistLong(title = '[Caboose Car] Long',
                             roster = 'pony',
                             base_numeric_id = 2210,
                             vehicle_generation = 1,
                                            speedy = True)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 0,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    consist = CabooseConsistShort(title = '[Caboose Car]',
                             roster = 'pony',
                             base_numeric_id = 1290,
                             vehicle_generation = 1,
                                            track_type = 'NG')

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 0,
                           vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)

"""
    #--------------- llama ----------------------------------------------------------------------
    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'llama',
                             base_numeric_id = 1300,
                             vehicle_generation = 1,
                                            speedy = True)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 0,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    #--------------- antelope ----------------------------------------------------------------------
    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'antelope',
                             base_numeric_id = 1780,
                             vehicle_generation = 1,
                                            speedy = True)

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 0,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'antelope',
                             base_numeric_id = 1880,
                             vehicle_generation = 1,
                                            speedy = True,
                             track_type = 'NG')

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 0,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


"""