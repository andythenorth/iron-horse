import global_constants
from train import FruitConsist, Wagon

def main():
    #--------------- antelope ----------------------------------------------------------------------
    consist = FruitConsist(title = '[Fruit Car]',
                           roster = 'antelope',
                           base_numeric_id = 2140,
                           wagon_generation = 1,
                           vehicle_life = 40,
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


    consist = FruitConsist(title = '[Fruit Car]',
                           roster = 'antelope',
                           base_numeric_id = 2170,
                           wagon_generation = 2,
                           vehicle_life = 40,
                           track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FruitConsist(title = '[Fruit Car]',
                           roster = 'antelope',
                           base_numeric_id = 2180,
                           wagon_generation = 3,
                           vehicle_life = 40,
                           track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
