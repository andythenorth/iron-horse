import global_constants
import graphics_processor.utils as graphics_utils
from train import HopperConsist, Wagon, GraphicsProcessorFactory

def get_graphics_processors(template):
    recolour_maps = graphics_utils.get_bulk_cargo_recolour_maps()
    graphics_options_master = {'template': '',
                               'recolour_maps': (recolour_maps),
                               'copy_block_top_offset': 30,
                               'num_rows_per_unit': 2,
                               'num_unit_types': 1}

    graphics_options_1 = dict((k, v) for (k, v) in graphics_options_master.items())
    graphics_options_1['template'] = template
    graphics_options_2 = dict((k, v) for (k, v) in graphics_options_1.items())
    graphics_options_2['swap_company_colours'] = True
    graphics_processor_1 = GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options_1)
    graphics_processor_2 = GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options_2)
    return (graphics_processor_1, graphics_processor_2)

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = HopperConsist(title = '[Hopper Car]',
                            roster = 'pony',
                            base_numeric_id = 1070,
                            wagon_generation = 1,
                                          intro_date = 1910,
                            vehicle_life = 40,
                            use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           weight = 10,
                           vehicle_length = 5))

    graphics_processors = get_graphics_processors('hopper_car_pony_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


    consist = HopperConsist(title = '[Hopper Car]',
                            roster = 'pony',
                            base_numeric_id = 1080,
                            wagon_generation = 2,
                                          intro_date = 1955,
                            vehicle_life = 40,
                            use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 55,
                           weight = 20,
                           vehicle_length = 8))

    graphics_processors = get_graphics_processors('hopper_car_pony_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


    consist = HopperConsist(title = '[Hopper Car]',
                            roster = 'pony',
                            base_numeric_id = 1090,
                            wagon_generation = 3,
                                          intro_date = 1995,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 75,
                           weight = 27,
                           vehicle_length = 10))

    graphics_processors = get_graphics_processors('hopper_car_pony_gen_3_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


    #--------------- llama ----------------------------------------------------------------------
    consist = HopperConsist(title = '[Rotary Gondola Car]',
                            roster = 'llama',
                            base_numeric_id = 1100,
                            wagon_generation = 2,
                                          intro_date = 1925,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 55,
                           weight = 20,
                           vehicle_length = 6))

    graphics_processors = get_graphics_processors('hopper_car_llama_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


    consist = HopperConsist(title = '[Hopper Car]',
                            roster = 'llama',
                            base_numeric_id = 1110,
                            wagon_generation = 3,
                                          intro_date = 1985,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 75,
                           weight = 25,
                           vehicle_length = 6))

    graphics_processors = get_graphics_processors('hopper_car_llama_gen_3_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])



    consist = HopperConsist(title = '[Rotary Gondola Car]',
                            roster = 'llama',
                            base_numeric_id = 1120,
                            wagon_generation = 2,
                                          intro_date = 1925,
                            vehicle_life = 40,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 45,
                           weight = 20,
                           vehicle_length = 6))

    graphics_processors = get_graphics_processors('hopper_car_ng_llama_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


    consist = HopperConsist(title = '[Hopper Car]',
                            roster = 'llama',
                            base_numeric_id = 1130,
                            wagon_generation = 3,
                                          intro_date = 1985,
                            vehicle_life = 40,
                            track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 65,
                           weight = 25,
                           vehicle_length = 6))

    graphics_processors = get_graphics_processors('hopper_car_ng_llama_gen_3_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


    #--------------- antelope ----------------------------------------------------------------------
    consist = HopperConsist(title = '[Rotary Gondola Car]',
                            roster = 'antelope',
                            base_numeric_id = 1630,
                            wagon_generation = 1,
                                          intro_date = 1950,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 60,
                           weight = 20,
                           vehicle_length = 6))

    graphics_processors = get_graphics_processors('hopper_car_antelope_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


    consist = HopperConsist(title = '[Rotary Gondola Car]',
                            roster = 'antelope',
                            base_numeric_id = 1660,
                            wagon_generation = 2,
                                          intro_date = 1985,
                            vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 75,
                           weight = 25,
                           vehicle_length = 6))

    graphics_processors = get_graphics_processors('hopper_car_antelope_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


    # no gen 1 NG hopper in Antelope, straight to gen 2
    consist = HopperConsist(title = '[Hopper Car]',
                            roster = 'antelope',
                            base_numeric_id = 1890,
                            wagon_generation = 2,
                                          intro_date = 1920,
                            vehicle_life = 40,
                            track_type = 'NG',
                            use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 35,
                           weight = 20,
                           vehicle_length = 6))

    graphics_processors = get_graphics_processors('hopper_car_ng_antelope_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=graphics_processors[1])


