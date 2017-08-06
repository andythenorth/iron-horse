import global_constants
from train import TankConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = TankConsist(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 630,
                      wagon_generation = 1,
                      intro_date = 1860,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 12,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 640,
                      wagon_generation = 2,
                      intro_date = 1960,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 27,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 650,
                      wagon_generation = 1,
                      intro_date = 1860,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            weight = 4,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 660,
                      wagon_generation = 1,
                      intro_date = 1860,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 670,
                      wagon_generation = 2,
                      intro_date = 1920,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 50,
                            weight = 18,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 680,
                      wagon_generation = 3,
                      intro_date = 1980,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 75,
                            weight = 12,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 690,
                      wagon_generation = 1,
                       intro_date = 1860,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 8,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 1360,
                      wagon_generation = 2,
                      intro_date = 1920,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 12,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = TankConsist(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1670,
                      wagon_generation = 1,
                      intro_date = 1950,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 18,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1680,
                      wagon_generation = 2,
                      intro_date = 1980,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 70,
                            weight = 35,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1910,
                      wagon_generation = 1,
                      intro_date = 1880,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 16,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1920,
                      wagon_generation = 2,
                      intro_date = 1925,
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


# gen 3 at 1980 or so
