import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

# cargo rows 0 indexed - 0 = first set of loaded sprites
cargo_graphics_mappings_normal = {'STEL': [1, 2, 3], 'WOOD': [4], 'WDPR': [5], 'ENSP': [6], 'FMSP': [6], 'MNSP': [6], 'GOOD': [0, 6]}

type_config_normal = TypeConfig(base_id = 'flat_car',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 7,
                    class_refit_groups = ['flatcar_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings_normal,
                    label_refits_allowed = cargo_graphics_mappings_normal.keys(),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_flatcar_freight'],
                    autorefit = True,
                    default_cargo = 'STEL',
                    default_capacity_type = 'capacity_freight')

# narrow gauge only different due to lack of diligence and suitable application to drawing sprites :P
# cargo rows 0 indexed - 0 = first set of loaded sprites
cargo_graphics_mappings_narrow_gauge = {'STEL': [1], 'WOOD': [2], 'WDPR': [3], 'ENSP': [4], 'FMSP': [4], 'MNSP': [4], 'GOOD': [0, 4]}

type_config_narrow_gauge = TypeConfig(base_id = 'flat_car_ng',
                    template = 'car_with_visible_cargo.pynml',
                    num_cargo_rows = 5,
                    class_refit_groups = ['flatcar_freight'],
                    cargo_graphics_mappings = cargo_graphics_mappings_narrow_gauge,
                    label_refits_allowed = cargo_graphics_mappings_narrow_gauge.keys(),
                    label_refits_disallowed = global_constants.disallowed_refits_by_label['non_flatcar_freight'],
                    autorefit = True,
                    default_cargo = 'STEL',
                    default_capacity_type = 'capacity_freight',
                    track_type = 'NG')

def main():
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 6,
                            vehicle_length = 5,
                            loading_speed = 10))

    options = {'template': 'flat_car_brit_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1950,
                        vehicle_life = 40,
                              use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 12,
                            vehicle_length = 8,
                            loading_speed = 10))

    options = {'template': 'flat_car_brit_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Flat Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1990,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 25,
                            vehicle_length = 10,
                            loading_speed = 5))

    options = {'template': 'flat_car_brit_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_narrow_gauge,
                        title = '[Flat Car]',
                        vehicle_set = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            weight = 3,
                            vehicle_length = 3,
                            loading_speed = 10))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)
