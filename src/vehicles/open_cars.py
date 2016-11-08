import global_constants
import graphics_processor.utils as graphics_utils
from train import OpenConsist, Wagon, GraphicsProcessorFactory

def get_graphics_processors(template):
    recolour_maps = graphics_utils.get_bulk_cargo_recolour_maps()
    graphics_options_master = {'template': 'filename.png',
                               'recolour_maps': (recolour_maps),
                               'copy_block_top_offset': 90,
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
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 820,
                          wagon_generation = 1,
                          replacement_id = '-none',
                          intro_date = 1860,
                          vehicle_life = 40,
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 7,
                            vehicle_length = 5))

    graphics_processors = get_graphics_processors('open_car_pony_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 830,
                          wagon_generation = 2,
                          replacement_id = '-none',
                          intro_date = 1950,
                          vehicle_life = 40,
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 15,
                            vehicle_length = 6))

    graphics_processors = get_graphics_processors('open_car_pony_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 840,
                          wagon_generation = 3,
                          replacement_id = '-none',
                          intro_date = 1997,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 25,
                            vehicle_length = 10))

    graphics_processors = get_graphics_processors('open_car_pony_gen_3_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 850,
                          wagon_generation = 1,
                          replacement_id = '-none',
                          intro_date = 1860,
                          vehicle_life = 40,
                          track_type = 'NG',
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            weight = 3,
                            vehicle_length = 3))

    graphics_processors = get_graphics_processors('open_car_ng_pony_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    #--------------- llama ----------------------------------------------------------------------
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 860,
                          wagon_generation = 1,
                          replacement_id = '-none',
                          intro_date = 1860,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 7,
                            vehicle_length = 5))

    graphics_processors = get_graphics_processors('open_car_llama_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 1330,
                          wagon_generation = 2,
                          replacement_id = '-none',
                          intro_date = 1920,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            weight = 15,
                            vehicle_length = 5))

    graphics_processors = get_graphics_processors('open_car_llama_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 870,
                          wagon_generation = 1,
                          replacement_id = '-none',
                          intro_date = 1860,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 3,
                            vehicle_length = 5))

    graphics_processors = get_graphics_processors('open_car_ng_llama_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 1320,
                          wagon_generation = 2,
                          replacement_id = '-none',
                          intro_date = 1920,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 3,
                            vehicle_length = 5))

    graphics_processors = get_graphics_processors('open_car_ng_llama_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    #--------------- antelope ----------------------------------------------------------------------
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1760,
                          wagon_generation = 1,
                          replacement_id = '-none',
                          intro_date = 1950,
                          vehicle_life = 40,
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 17,
                            vehicle_length = 5))

    graphics_processors = get_graphics_processors('open_car_antelope_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1770,
                          wagon_generation = 2,
                          replacement_id = '-none',
                          intro_date = 1980,
                          vehicle_life = 40,
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 70,
                            weight = 22,
                            vehicle_length = 8))

    graphics_processors = get_graphics_processors('open_car_antelope_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 2090,
                          wagon_generation = 1,
                          replacement_id = '-none',
                          intro_date = 1860,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 10,
                            vehicle_length = 5))

    graphics_processors = get_graphics_processors('open_car_ng_antelope_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1830,
                          wagon_generation = 2,
                          replacement_id = '-none',
                          intro_date = 1915,
                          vehicle_life = 40,
                          track_type = 'NG',
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 12,
                            vehicle_length = 6))

    graphics_processors = get_graphics_processors('open_car_ng_antelope_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1820,
                          wagon_generation = 3,
                          replacement_id = '-none',
                          intro_date = 1970,
                          vehicle_life = 40,
                          track_type = 'NG',
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 18,
                            vehicle_length = 6))

    graphics_processors = get_graphics_processors('open_car_ng_antelope_gen_3_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


