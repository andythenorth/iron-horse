import global_constants
from train import EdiblesTankConsist, FreightCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = EdiblesTankConsist(roster = 'pony',
                                 base_numeric_id = 1190,
                                 vehicle_generation = 1,
                                                    speedy = True)

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 25,
                           vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankConsist(roster = 'pony',
                                 base_numeric_id = 1200,
                                 vehicle_generation = 3,
                                                    speedy = True)

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 40,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = EdiblesTankConsist(roster = 'llama',
                                 base_numeric_id = 1210,
                                 vehicle_generation = 1)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 25,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankConsist(roster = 'llama',
                                 base_numeric_id = 1220,
                                 vehicle_generation = 3,
                                                    speedy = True)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 55,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = EdiblesTankConsist(roster = 'antelope',
                        base_numeric_id = 1690,
                        vehicle_generation = 1)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 45,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = EdiblesTankConsist(roster = 'antelope',
                                 base_numeric_id = 1700,
                                 vehicle_generation = 2,
                                                    speedy = True)

    consist.add_unit(FreightCar(consist = consist,
                            capacity = 60,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])

