import global_constants
import graphics_processor.utils as graphics_utils
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

# cargo rows 0 indexed - 0 = first set of loaded sprites
# GRVL is in first position as it is re-used for generic unknown cargos
# hoppers *do* transport SCMT in this set, realism is not relevant here, went back and forth on this a few times :P
cargo_graphics_mappings = {'GRVL': [0], 'IORE': [1], 'CORE': [2], 'AORE': [3],
                           'SAND': [4], 'COAL': [5], 'CLAY': [6], 'SCMT': [7], 'PHOS': [8]}

type_config_normal = TypeConfig(base_id = 'hopper_car',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 9, # update if more cargo graphic variations are added
                    class_refit_groups = ['hopper_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = list(cargo_graphics_mappings.keys()),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_hopper_freight'],
                    autorefit = True,
                    default_cargo = 'COAL',
                    default_capacity_type = 'capacity_freight',
                    loading_speed_multiplier = 2)

type_config_narrow_gauge = TypeConfig(base_id = 'hopper_car_ng',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 9, # update if more cargo graphic variations are added
                    class_refit_groups = ['hopper_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings,
                    label_refits_allowed = list(cargo_graphics_mappings.keys()),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_hopper_freight'],
                    autorefit = True,
                    default_cargo = 'COAL',
                    default_capacity_type = 'capacity_freight',
                    track_type = 'NG',
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
    #--------------- pony ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Hopper Car]',
                        roster = 'pony',
                        base_numeric_id = 1070,
                        wagon_generation = 1,
                        replacement_id = '-none',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Hopper Car]',
                        roster = 'pony',
                        base_numeric_id = 1080,
                        wagon_generation = 2,
                        replacement_id = '-none',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Hopper Car]',
                        roster = 'pony',
                        base_numeric_id = 1090,
                        wagon_generation = 3,
                        replacement_id = '-none',
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
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Rotary Gondola Car]',
                        roster = 'llama',
                        base_numeric_id = 1100,
                        wagon_generation = 2,
                        replacement_id = '-none',
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


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Hopper Car]',
                        roster = 'llama',
                        base_numeric_id = 1110,
                        wagon_generation = 3,
                        replacement_id = '-none',
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



    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Rotary Gondola Car]',
                        roster = 'llama',
                        base_numeric_id = 1120,
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1925,
                        vehicle_life = 40)

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


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Hopper Car]',
                        roster = 'llama',
                        base_numeric_id = 1130,
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1985,
                        vehicle_life = 40)

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


