import global_constants
from train import LogConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = LogConsist(title = '[Log Car]',
                          roster = 'pony',
                          base_numeric_id = 1710,
                          wagon_generation = 4,
                          intro_date = 1990,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = LogConsist(title = '[Log Car]',
                          roster = 'pony',
                          base_numeric_id = 930,
                          wagon_generation = 5,
                          intro_date = 2020,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])    #--------------- antelope ----------------------------------------------------------------------

    #--------------- llama ----------------------------------------------------------------------


