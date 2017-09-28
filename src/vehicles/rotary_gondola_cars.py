import global_constants
from train import DumpConsist, FreightCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = DumpConsist(roster = 'pony',
                            base_numeric_id = 1340,
                            vehicle_generation = 3)

    consist.add_unit(type = FreightCar,
                           capacity = 20,
                           vehicle_length = 4)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = DumpConsist(roster = 'pony',
                            base_numeric_id = 1810,
                            vehicle_generation = 4)

    consist.add_unit(type = FreightCar,
                           capacity = 40,
                           vehicle_length = 6)

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date = 0,
                              end_date = global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
