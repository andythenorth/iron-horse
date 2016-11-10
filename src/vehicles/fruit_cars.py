import global_constants
from train import FruitConsist, Wagon, GraphicsProcessorFactory

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

    options = {'template': 'fruit_car_ng_antelope_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


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

    options = {'template': 'fruit_car_ng_antelope_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


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

    options = {'template': 'fruit_car_ng_antelope_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

