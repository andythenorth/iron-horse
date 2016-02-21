import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

# cargo rows 0 indexed - 0 = first set of loaded sprites
cargo_graphics_mappings = {'VEHI': [0, 1]}

type_config = TypeConfig(base_id = 'vehicle_transporter_car',
                        template = 'car_with_visible_cargo.pynml',
                        num_cargo_rows = 2,
                        class_refit_groups = [],
                        cargo_graphics_mappings = cargo_graphics_mappings,
                        label_refits_allowed = list(cargo_graphics_mappings.keys()),
                        label_refits_disallowed = [],
                        autorefit = True,
                        default_cargo = 'VEHI',
                        default_capacity_type = 'capacity_freight',
                        date_variant_var = 'current_year')

def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = WagonConsist(type_config = type_config,
                        title = '[Vehicle Transporter Car]',
                        roster = 'pony',
                        base_numeric_id = 1530,
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1960,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 12,
                            vehicle_length = 7))

    options = {'template': 'vehicle_transporter_car_pony_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))
