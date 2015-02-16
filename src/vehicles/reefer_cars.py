import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

cargo_graphics_mappings = {} # template needs this, but reefer car has zero cargo-specific graphics, all generic

type_config = TypeConfig(base_id = 'reefer_car',
                        template = 'car_with_open_doors_during_loading.pynml',
                        num_cargo_rows = 1, # template needs this, but box car has zero cargo-specific graphics, all generic
                        cargo_graphics_mappings = cargo_graphics_mappings,
                        class_refit_groups = ['refrigerated_freight'],
                        label_refits_allowed = [],
                        label_refits_disallowed = [],
                        autorefit = True,
                        default_cargo = 'FOOD',
                        default_capacity_type = 'capacity_freight',
                        cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD)

def main():
    consist = WagonConsist(type_config = type_config,
                        title = '[Reefer Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1915,
                        vehicle_life = 40,
                        speedy = True,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 14,
                            vehicle_length = 6))

    options = {'template': 'reefer_car_brit_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    # no gen 2 reefer - straight to gen 3
    consist = WagonConsist(type_config = type_config,
                        title = '[Reefer Car]',
                        roster = 'brit',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1964,
                        vehicle_life = 40,
                        speedy = True,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 30,
                            vehicle_length = 8))

    options = {'template': 'reefer_car_brit_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))
