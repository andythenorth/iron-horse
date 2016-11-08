import global_constants
from train import TankCar, Wagon, GraphicsProcessorFactory

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = TankCar(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 630,
                      wagon_generation = 1,
                      replacement_id = '-none',
                      intro_date = 1860,
                      vehicle_life = 40,
                      use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'tank_car_pony_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 640,
                      wagon_generation = 2,
                      replacement_id = '-none',
                      intro_date = 1960,
                      vehicle_life = 40,
                      use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 27,
                            vehicle_length = 8))

    options = {'template': 'tank_car_pony_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 650,
                      wagon_generation = 1,
                      replacement_id = '-none',
                      intro_date = 1860,
                      vehicle_life = 40,
                      track_type = 'NG',
                      use_legacy_spritesheet = True)

    options = {'template': 'tank_car_ng_pony_gen_1_template.png'}

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            weight = 4,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- llama ----------------------------------------------------------------------
    consist = TankCar(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 660,
                      wagon_generation = 1,
                      replacement_id = '-none',
                      intro_date = 1860,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'tank_car_llama_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 670,
                      wagon_generation = 2,
                      replacement_id = '-none',
                      intro_date = 1920,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 50,
                            weight = 18,
                            vehicle_length = 5))

    options = {'template': 'tank_car_llama_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 680,
                      wagon_generation = 3,
                      replacement_id = '-none',
                      intro_date = 1980,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 75,
                            weight = 12,
                            vehicle_length = 8))

    options = {'template': 'tank_car_llama_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 690,
                      wagon_generation = 1,
                      replacement_id = '-none',
                      intro_date = 1860,
                      vehicle_life = 40,
                      track_type = 'NG')

    options = {'template': 'tank_car_ng_llama_gen_1_template.png'}

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 8,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 1360,
                      wagon_generation = 2,
                      replacement_id = '-none',
                      intro_date = 1920,
                      vehicle_life = 40,
                      track_type = 'NG')

    options = {'template': 'tank_car_ng_llama_gen_1_template.png'}

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 12,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- antelope ----------------------------------------------------------------------
    consist = TankCar(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1670,
                      wagon_generation = 1,
                      replacement_id = '-none',
                      intro_date = 1950,
                      vehicle_life = 40,
                      use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 18,
                            vehicle_length = 6))

    options = {'template': 'tank_car_antelope_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1680,
                      wagon_generation = 2,
                      replacement_id = '-none',
                      intro_date = 1980,
                      vehicle_life = 40,
                      use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 70,
                            weight = 35,
                            vehicle_length = 8))

    options = {'template': 'tank_car_antelope_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1910,
                      wagon_generation = 1,
                      replacement_id = '-none',
                      intro_date = 1880,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 16,
                            vehicle_length = 5))

    options = {'template': 'tank_car_ng_antelope_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = TankCar(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1920,
                      wagon_generation = 2,
                      replacement_id = '-none',
                      intro_date = 1925,
                      vehicle_life = 40,
                      track_type = 'NG',
                      use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 20,
                            vehicle_length = 6))

    options = {'template': 'tank_car_ng_antelope_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


# gen 3 at 1980 or so
