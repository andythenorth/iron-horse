import global_constants
from train import OpenConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 820,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 7,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 830,
                          wagon_generation = 2,
                          intro_date = 1950,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 15,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 840,
                          wagon_generation = 3,
                          intro_date = 1997,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 25,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 850,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 12,
                           weight = 4,
                           vehicle_length = 3))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 860,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 7,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 1330,
                          wagon_generation = 2,
                          intro_date = 1920,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            weight = 15,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 870,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 3,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 1320,
                          wagon_generation = 2,
                          intro_date = 1920,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 3,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1760,
                          wagon_generation = 1,
                          intro_date = 1950,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 17,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1770,
                          wagon_generation = 2,
                          intro_date = 1980,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 70,
                            weight = 22,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 2090,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 10,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1830,
                          wagon_generation = 2,
                          intro_date = 1915,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 12,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1820,
                          wagon_generation = 3,
                          intro_date = 1970,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 18,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
