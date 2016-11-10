import global_constants
from train import FruitConsist, Wagon

def main():
    #--------------- antelope ----------------------------------------------------------------------
    consist = FruitConsist(title = '[Fruit Car]',
                           roster = 'antelope',
                           base_numeric_id = 2140,
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
                           spritesheet_suffix=0,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FruitConsist(title = '[Fruit Car]',
                           roster = 'antelope',
                           base_numeric_id = 2170,
                           wagon_generation = 2,
                           intro_date = 1915,
                           vehicle_life = 40,
                           track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 14,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = FruitConsist(title = '[Fruit Car]',
                           roster = 'antelope',
                           base_numeric_id = 2180,
                           wagon_generation = 3,
                           intro_date = 1970,
                           vehicle_life = 40,
                           track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 18,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
