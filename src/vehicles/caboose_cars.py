import global_constants
from train import CabooseConsistShort, CabooseConsistLong, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CabooseConsistShort(title = '[Caboose Car] Short',
                             roster = 'pony',
                             base_numeric_id = 1280,
                             wagon_generation = 1,
                             intro_date = 1860,
                             vehicle_life = 40,
                             speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 0,
                            weight = 20,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = CabooseConsistLong(title = '[Caboose Car] Long',
                             roster = 'pony',
                             base_numeric_id = 2210,
                             wagon_generation = 1,
                             intro_date = 1860,
                             vehicle_life = 40,
                             speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 0,
                            weight = 20,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = CabooseConsistShort(title = '[Caboose Car]',
                             roster = 'pony',
                             base_numeric_id = 1290,
                             wagon_generation = 1,
                             intro_date = 1860,
                             vehicle_life = 40,
                             track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 0,
                           weight = 10,
                           vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)

"""
    #--------------- llama ----------------------------------------------------------------------
    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'llama',
                             base_numeric_id = 1300,
                             wagon_generation = 1,
                             intro_date = 1860,
                             vehicle_life = 40,
                             speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 0,
                            weight = 20,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    #--------------- antelope ----------------------------------------------------------------------
    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'antelope',
                             base_numeric_id = 1780,
                             wagon_generation = 1,
                             intro_date = 1950,
                             vehicle_life = 50,
                             speedy = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 0,
                           weight = 40,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = CabooseConsist(title = '[Caboose Car]',
                             roster = 'antelope',
                             base_numeric_id = 1880,
                             wagon_generation = 1,
                             intro_date = 1860,
                             vehicle_life = 50,
                             speedy = True,
                             track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 0,
                           weight = 25,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


"""