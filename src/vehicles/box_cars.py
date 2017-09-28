import global_constants
from train import BoxConsistShort, BoxConsistLong, BoxCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = BoxConsistShort(roster = 'pony',
                         base_numeric_id = 1780,
                         vehicle_generation = 1)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'pony',
                              base_numeric_id = 550,
                              vehicle_generation = 2)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'pony',
                              base_numeric_id = 560,
                              vehicle_generation = 3)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 35,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistLong(    roster = 'pony',
                             base_numeric_id = 2340,
                             vehicle_generation = 3)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 55,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'pony',
                             base_numeric_id = 570,
                             vehicle_generation = 4)

    consist.add_unit(BoxCar(consist = consist,
                                capacity_freight = 55,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'pony',
                         base_numeric_id = 580,
                         vehicle_generation = 1,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 12,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = BoxConsistShort(roster = 'llama',
                        base_numeric_id = 590,
                        vehicle_generation = 1)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'llama',
                         base_numeric_id = 600,
                         vehicle_generation = 2)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 45,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'llama',
                         base_numeric_id = 610,
                         vehicle_generation = 3)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 65,
                            vehicle_length = 7))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'llama',
                        base_numeric_id = 620,
                        vehicle_generation = 1,
                                  track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'llama',
                         base_numeric_id = 1310,
                         vehicle_generation = 2,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 35,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = BoxConsistShort(roster = 'antelope',
                         base_numeric_id = 1750,
                         vehicle_generation = 1)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 55,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'antelope',
                         base_numeric_id = 1740,
                         vehicle_generation = 2)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 70,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'antelope',
                         base_numeric_id = 2100,
                         vehicle_generation = 1,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'antelope',
                         base_numeric_id = 1850,
                         vehicle_generation = 2,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 30,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(roster = 'antelope',
                         base_numeric_id = 1860,
                         vehicle_generation = 3,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 40,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


