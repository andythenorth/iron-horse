import global_constants
from train import LivestockConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'pony',
                               base_numeric_id = 1010,
                               vehicle_generation = 1)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'pony',
                               base_numeric_id = 1020,
                               vehicle_generation = 2)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'pony',
                               base_numeric_id = 1030,
                               vehicle_generation = 1,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------
    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'llama',
                               base_numeric_id = 1040,
                               vehicle_generation = 1)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'llama',
                               base_numeric_id = 1430,
                               vehicle_generation = 2)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'llama',
                               base_numeric_id = 1050,
                               vehicle_generation = 1,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'llama',
                               base_numeric_id = 1520,
                               vehicle_generation = 2,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    #--------------- antelope ----------------------------------------------------------------------
    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'antelope',
                               base_numeric_id = 1720,
                               vehicle_generation = 1)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'antelope',
                               base_numeric_id = 2150,
                               vehicle_generation = 1,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)

