import global_constants
from train import DumpConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = DumpConsist(title = '[Dump Car]',
                            roster = 'pony',
                            base_numeric_id = 1340,
                            vehicle_generation = 3)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 20,
                           vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = DumpConsist(title = '[Dump Car]',
                            roster = 'pony',
                            base_numeric_id = 1810,
                            vehicle_generation = 4)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])

    #--------------- llama ----------------------------------------------------------------------

    #--------------- antelope ----------------------------------------------------------------------
