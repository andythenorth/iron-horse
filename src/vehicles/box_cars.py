import global_constants
from train import BoxConsist, BoxCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = BoxConsist(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 60,
                         wagon_generation = 1,
                         intro_date = 1860,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 30,
                            weight = 12,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 550,
                         wagon_generation = 2,
                         intro_date = 1930,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 30,
                            weight = 12,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 560,
                         wagon_generation = 3,
                         intro_date = 1960,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 35,
                            capacity_mail = 45,
                            weight = 18,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 570,
                         wagon_generation = 4,
                         intro_date = 1990,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 55,
                            capacity_mail = 65,
                            weight = 25,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'pony',
                         base_numeric_id = 580,
                         wagon_generation = 1,
                                    intro_date = 1860,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 12,
                            capacity_mail = 20,
                            weight = 5,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = BoxConsist(title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 590,
                        wagon_generation = 1,
                                  intro_date = 1860,
                        vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 25,
                            capacity_mail = 35,
                            weight = 12,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'llama',
                         base_numeric_id = 600,
                         wagon_generation = 2,
                                    intro_date = 1920,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 45,
                            capacity_mail = 55,
                            weight = 20,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'llama',
                         base_numeric_id = 610,
                         wagon_generation = 3,
                                    intro_date = 1980,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 65,
                            capacity_mail = 75,
                            weight = 30,
                            vehicle_length = 7))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                        roster = 'llama',
                        base_numeric_id = 620,
                        wagon_generation = 1,
                                  intro_date = 1860,
                        vehicle_life = 40,
                        track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 20,
                            weight = 10,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'llama',
                         base_numeric_id = 1310,
                         wagon_generation = 2,
                                    intro_date = 1920,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 35,
                            capacity_mail = 35,
                            weight = 15,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = BoxConsist(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 1750,
                         wagon_generation = 1,
                                    intro_date = 1950,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 55,
                            capacity_mail = 75,
                            weight = 18,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 1740,
                         wagon_generation = 2,
                                    intro_date = 1981,
                         vehicle_life = 40)

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 70,
                            capacity_mail = 100,
                            weight = 32,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 2100,
                         wagon_generation = 1,
                                    intro_date = 1860,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 20,
                            capacity_mail = 27,
                            weight = 15,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 1850,
                         wagon_generation = 2,
                                    intro_date = 1915,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 30,
                            capacity_mail = 40,
                            weight = 19,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = BoxConsist(title = '[Box Car]',
                         roster = 'antelope',
                         base_numeric_id = 1860,
                         wagon_generation = 3,
                                    intro_date = 1970,
                         vehicle_life = 40,
                         track_type = 'NG')

    consist.add_unit(BoxCar(consist = consist,
                            capacity_freight = 40,
                            capacity_mail = 55,
                            weight = 22,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


