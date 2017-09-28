import global_constants
from train import EdiblesTankConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'pony',
                                 base_numeric_id = 1190,
                                 wagon_generation = 1,
                                 intro_date = 1905,
                                 vehicle_life = 40,
                                 speedy = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 25,
                           vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'pony',
                                 base_numeric_id = 1200,
                                 wagon_generation = 3,
                                 intro_date = 1988,
                                 vehicle_life = 40,
                                 speedy = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'llama',
                                 base_numeric_id = 1210,
                                 wagon_generation = 1,
                                                    intro_date = 1905,
                                 vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'llama',
                                 base_numeric_id = 1220,
                                 wagon_generation = 3,
                                                    intro_date = 1988,
                                 vehicle_life = 40,
                                 speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                        roster = 'antelope',
                        base_numeric_id = 1690,
                        wagon_generation = 1,
                                  intro_date = 1950,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = EdiblesTankConsist(title = '[Edibles Tank Car]',
                                 roster = 'antelope',
                                 base_numeric_id = 1700,
                                 wagon_generation = 2,
                                                    intro_date = 1981,
                                 vehicle_life = 40,
                                 speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 60,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])

