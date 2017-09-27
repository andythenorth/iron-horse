import global_constants
from train import CoalConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CoalConsist(title = '[Coal Car]',
                            roster = 'pony',
                            base_numeric_id = 2320,
                            wagon_generation = 1,
                            intro_date = 1960,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           weight = 10,
                           vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = CoalConsist(title = '[Coal Car]',
                            roster = 'pony',
                            base_numeric_id = 2310,
                            wagon_generation = 2,
                            intro_date = 1960,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           weight = 10,
                           vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = CoalConsist(title = '[Coal Car]',
                            roster = 'pony',
                            base_numeric_id = 1380,
                            wagon_generation = 3,
                            intro_date = 1960,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           weight = 10,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
