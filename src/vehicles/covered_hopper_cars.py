import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

type_config = TypeConfig(base_id = 'covered_hopper_car',
                template = 'train.pynml',
                class_refit_groups = ['covered_hopper_freight'],
                label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ', 'FOOD', 'SUGR', 'FMSP', 'RFPR', 'CLAY', 'BDMT', 'BEAN', 'NITR'],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GRAI',
                default_capacity_type = 'capacity_freight',
                loading_speed_multiplier = 2)

def main():
    #--------------- brit ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config,
                        title = '[Covered Hopper Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1922,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'covered_hopper_car_brit_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config,
                        title = '[Covered Hopper Car]',
                        roster = 'brit',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1955,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 18,
                            vehicle_length = 6))

    options = {'template': 'covered_hopper_car_brit_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config,
                        title = '[Covered Hopper Car]',
                        roster = 'brit',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1985,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 60,
                            weight = 27,
                            vehicle_length = 8))

    options = {'template': 'covered_hopper_car_brit_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- soam ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config,
                        title = '[Covered Hopper Car]',
                        roster = 'soam',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1955,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 18,
                            vehicle_length = 7))

    options = {'template': 'covered_hopper_car_soam_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

