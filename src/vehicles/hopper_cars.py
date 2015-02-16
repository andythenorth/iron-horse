import global_constants
import graphics_processor.utils as graphics_utils
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

# cargo rows 0 indexed - 0 = first set of loaded sprites
cargo_graphics_mappings = {'AORE': [0], 'IORE': [1], 'CORE': [2], 'GRVL': [3],
                           'SAND': [4], 'COAL': [5], 'CLAY': [6]}

type_config_normal = TypeConfig(base_id = 'hopper_car',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 7,
                    class_refit_groups = ['hopper_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = cargo_graphics_mappings.keys(),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_hopper_freight'],
                    autorefit = True,
                    default_cargo = 'COAL',
                    default_capacity_type = 'capacity_freight',
                    loading_speed_multiplier = 2)

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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Hopper Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1910,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 10,
                            vehicle_length = 5))

    graphics_processors = get_graphics_processors('hopper_car_brit_gen_1_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Hopper Car]',
                        roster = 'brit',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1955,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 20,
                            vehicle_length = 8))

    graphics_processors = get_graphics_processors('hopper_car_brit_gen_2_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Hopper Car]',
                        roster = 'brit',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1995,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 75,
                            weight = 27,
                            vehicle_length = 10))

    graphics_processors = get_graphics_processors('hopper_car_brit_gen_3_template.png')

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=graphics_processors[0])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=graphics_processors[1])
