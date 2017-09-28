import global_constants
from train import BoxConsistShort, BoxConsistLong, BoxCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 1780,
                         wagon_generation = 1,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 30,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 550,
                         wagon_generation = 2,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 30,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 560,
                         wagon_generation = 3,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 35,
                            capacity_mail = 45,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistLong(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 2340,
                         wagon_generation = 3,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 55,
                            capacity_mail = 65,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 570,
                         wagon_generation = 4,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 55,
                            capacity_mail = 65,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 580,
                         wagon_generation = 1,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 12,
                            capacity_mail = 20,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = BoxConsistShort(title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 590,
                        wagon_generation = 1,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 25,
                            capacity_mail = 35,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'llama',
                         base_numeric_id = 600,
                         wagon_generation = 2,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 45,
                            capacity_mail = 55,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'llama',
                         base_numeric_id = 610,
                         wagon_generation = 3,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 65,
                            capacity_mail = 75,
                            vehicle_length = 7))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 620,
                        wagon_generation = 1,
                        vehicle_life = 40,
                        track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 20,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'llama',
                         base_numeric_id = 1310,
                         wagon_generation = 2,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 35,
                            capacity_mail = 35,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 1750,
                         wagon_generation = 1,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 55,
                            capacity_mail = 75,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 1740,
                         wagon_generation = 2,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 70,
                            capacity_mail = 100,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 2100,
                         wagon_generation = 1,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 27,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 1850,
                         wagon_generation = 2,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 30,
                            capacity_mail = 40,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsistShort(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 1860,
                         wagon_generation = 3,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 40,
                            capacity_mail = 55,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


