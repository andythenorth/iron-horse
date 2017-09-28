import global_constants
from train import LogConsist, FreightCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = LogConsist(roster = 'pony',
                          base_numeric_id = 1710,
                          vehicle_generation = 4)

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 30,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = LogConsist(roster = 'pony',
                          base_numeric_id = 930,
                          vehicle_generation = 5)

    consist.add_unit(FreightCar(consist = consist,
                           capacity = 30,
                           vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])    #--------------- antelope ----------------------------------------------------------------------

    #--------------- llama ----------------------------------------------------------------------


