import global_constants
from train import FlatConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1140,
                           vehicle_generation = 1)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1150,
                           vehicle_generation = 2)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1160,
                           vehicle_generation = 3)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 50,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1170,
                           vehicle_generation = 1,
                                        track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 12,
                           vehicle_length = 3))

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------
    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'llama',
                           base_numeric_id = 1180,
                           vehicle_generation = 1)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 25,
                           vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'llama',
                           base_numeric_id = 1510,
                           vehicle_generation = 2)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 45,
                           vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'llama',
                           base_numeric_id = 520,
                           vehicle_generation = 1,
                                        track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'llama',
                           base_numeric_id = 1500,
                           vehicle_generation = 2,
                                        track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 35,
                           vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'antelope',
                           base_numeric_id = 1640,
                           vehicle_generation = 1)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 55,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'antelope',
                           base_numeric_id = 1650,
                           vehicle_generation = 2)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 70,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'antelope',
                           base_numeric_id = 2110,
                           vehicle_generation = 1,
                                        track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FlatConsist(title = '[Flat Car]',
                           roster = 'antelope',
                           base_numeric_id = 1930,
                           vehicle_generation = 2,
                                        track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
