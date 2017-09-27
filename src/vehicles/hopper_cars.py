import global_constants
from train import HopperConsistShort, HopperConsistLong, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = HopperConsistShort(title = '[Hopper Car]',
                                 roster = 'pony',
                                 base_numeric_id = 1070,
                                 wagon_generation = 3,
                                 intro_date = 1960,
                                 vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           weight = 10,
                           vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistLong(title = '[Hopper Car]',
                                 roster = 'pony',
                                 base_numeric_id = 2330,
                                 wagon_generation = 3,
                                 intro_date = 1960,
                                 vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           weight = 10,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Hopper Car]',
                            roster = 'pony',
                            base_numeric_id = 1080,
                            wagon_generation = 4,
                            intro_date = 1990,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           weight = 20,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistLong(title = '[Hopper Car]',
                            roster = 'pony',
                            base_numeric_id = 1090,
                            wagon_generation = 4,
                            intro_date = 1990,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           weight = 25,
                           vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = HopperConsistShort(title = '[Rotary Gondola Car]',
                            roster = 'llama',
                            base_numeric_id = 1100,
                            wagon_generation = 2,
                                          intro_date = 1925,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 55,
                           weight = 20,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Hopper Car]',
                            roster = 'llama',
                            base_numeric_id = 1110,
                            wagon_generation = 3,
                                          intro_date = 1985,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 75,
                           weight = 25,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Rotary Gondola Car]',
                            roster = 'llama',
                            base_numeric_id = 1120,
                            wagon_generation = 2,
                                          intro_date = 1925,
                            vehicle_life = 40,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 45,
                           weight = 20,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Hopper Car]',
                            roster = 'llama',
                            base_numeric_id = 1130,
                            wagon_generation = 3,
                                          intro_date = 1985,
                            vehicle_life = 40,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 65,
                           weight = 25,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = HopperConsistShort(title = '[Rotary Gondola Car]',
                            roster = 'antelope',
                            base_numeric_id = 1630,
                            wagon_generation = 1,
                                          intro_date = 1950,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 60,
                           weight = 20,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = HopperConsistShort(title = '[Rotary Gondola Car]',
                            roster = 'antelope',
                            base_numeric_id = 1660,
                            wagon_generation = 2,
                                          intro_date = 1985,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 75,
                           weight = 25,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    # no gen 1 NG hopper in Antelope, straight to gen 2
    consist = HopperConsistShort(title = '[Hopper Car]',
                            roster = 'antelope',
                            base_numeric_id = 1890,
                            wagon_generation = 2,
                                          intro_date = 1920,
                            vehicle_life = 40,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 35,
                           weight = 20,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


