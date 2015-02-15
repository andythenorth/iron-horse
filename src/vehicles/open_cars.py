import global_constants
import graphics_processor.utils as graphics_utils
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory


b = 1 # bulk cargo start row
# cargo rows 0 indexed - 0 = first set of loaded sprites
cargo_graphics_mappings = {'AORE': [b], 'IORE': [b + 1], 'CORE': [b + 2], 'GRVL': [b + 3],
                           'SAND': [b + 4], 'COAL': [b + 5], 'CLAY': [b + 6]}


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
    # Normal Railtype
    type_config = TypeConfig(base_id = 'open_car',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 8,
                    class_refit_groups = ['all_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = cargo_graphics_mappings.keys(),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases'],
                    autorefit = True,
                    default_cargo = 'GOOD',
                    default_capacity_type = 'capacity_freight')


    consist = WagonConsist(type_config = type_config,
                        title = '[Open Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                              use_legacy_spritesheet = True)

    consist.add_unit(Wagon(type_config = type_config,
                            consist = consist,
                            capacity_freight = 20,
                            weight = 7,
                            vehicle_length = 5,
                            loading_speed = 10))

    graphics_processors = get_graphics_processors('open_car_brit_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = WagonConsist(type_config = type_config,
                        title = '[Open Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1950,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(type_config = type_config,
                            consist = consist,
                            capacity_freight = 35,
                            weight = 15,
                            vehicle_length = 6,
                            loading_speed = 10))

    graphics_processors = get_graphics_processors('open_car_brit_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])



    consist = WagonConsist(type_config = type_config,
                        title = '[Open Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1997,
                        vehicle_life = 40)

    consist.add_unit(Wagon(type_config = type_config,
                            consist = consist,
                            capacity_freight = 55,
                            weight = 25,
                            vehicle_length = 10,
                            loading_speed = 10))

    graphics_processors = get_graphics_processors('open_car_brit_gen_3_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = WagonConsist(type_config = type_config,
                        title = '[Open Car]',
                        vehicle_set = 'soam',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40)

    consist.add_unit(Wagon(type_config = type_config,
                            consist = consist,
                            capacity_freight = 30,
                            weight = 7,
                            vehicle_length = 5,
                            loading_speed = 10))

    graphics_processors = get_graphics_processors('open_car_soam_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    # Narrow Gauge Railtype
    type_config = TypeConfig(base_id = 'open_car_ng',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 8,
                    class_refit_groups = ['all_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = cargo_graphics_mappings.keys(),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_freight_special_cases'],
                    autorefit = True,
                    default_cargo = 'GOOD',
                    default_capacity_type = 'capacity_freight',
                    track_type = 'NG')

    consist = WagonConsist(type_config = type_config,
                        title = '[Open Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                              use_legacy_spritesheet = True)

    consist.add_unit(Wagon(type_config = type_config,
                            consist = consist,
                            capacity_freight = 12,
                            weight = 3,
                            vehicle_length = 3,
                            loading_speed = 5))

    graphics_processors = get_graphics_processors('open_car_ng_brit_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])

