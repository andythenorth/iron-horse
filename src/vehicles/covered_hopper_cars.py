import global_constants
from train import CoveredHopperConsist, Wagon, GraphicsProcessorFactory

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperConsist(title = '[Covered Hopper Car]',
                                   roster = 'pony',
                                   base_numeric_id = 1270,
                                   wagon_generation = 1,
                                   replacement_id = '-none',
                                   intro_date = 1922,
                                   vehicle_life = 40,
                                   use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 25,
                           weight = 12,
                           vehicle_length = 5))

    options = {'template': 'covered_hopper_car_pony_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = CoveredHopperConsist(title = '[Covered Hopper Car]',
                                   roster = 'pony',
                                   base_numeric_id = 1230,
                                   wagon_generation = 2,
                                   replacement_id = '-none',
                                   intro_date = 1955,
                                   vehicle_life = 40,
                                   use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 40,
                           weight = 18,
                           vehicle_length = 6))

    options = {'template': 'covered_hopper_car_pony_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = CoveredHopperConsist(title = '[Covered Hopper Car]',
                                   roster = 'pony',
                                   base_numeric_id = 1240,
                                   wagon_generation = 3,
                                   replacement_id = '-none',
                                   intro_date = 1985,
                                   vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 60,
                           weight = 27,
                           vehicle_length = 8))

    options = {'template': 'covered_hopper_car_pony_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- llama ----------------------------------------------------------------------
    consist = CoveredHopperConsist(title = '[Covered Hopper Car]',
                                   roster = 'llama',
                                   base_numeric_id = 1250,
                                   wagon_generation = 2,
                                   replacement_id = '-none',
                                   intro_date = 1955,
                                   vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 18,
                            vehicle_length = 7))

    options = {'template': 'covered_hopper_car_llama_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = CoveredHopperConsist(title = '[Covered Hopper Car]',
                                   roster = 'llama',
                                   base_numeric_id = 1260,
                                   wagon_generation = 3,
                                   replacement_id = '-none',
                                   intro_date = 1985,
                                   vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 65,
                           weight = 27,
                           vehicle_length = 8))

    options = {'template': 'covered_hopper_car_llama_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

