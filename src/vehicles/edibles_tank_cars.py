import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

# tank cars are unrealistically autorefittable, and at no cost
# Pikka: if people complain that it's unrealistic, tell them "don't do it then"
type_config = TypeConfig(base_id = 'edibles_tank_car',
                template = 'train.pynml',
                class_refit_groups = ['liquids'],
                label_refits_allowed = ['FOOD'],
                label_refits_disallowed = global_constants.disallowed_refits_by_label['non_edible_liquids'],
                autorefit = True,
                default_cargo = 'WATR',
                default_capacity_type = 'capacity_freight',
                cargo_age_period = 2 * global_constants.CARGO_AGE_PERIOD,
                loading_speed_multiplier = 2)

def main():
    #--------------- brit ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config,
                        title = '[Edibles Tank Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1905,
                        vehicle_life = 40,
                        speedy = True,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'edibles_tank_car_brit_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

    # no gen 2 for edibles tank cars - straight to gen 3

    consist = WagonConsist(type_config = type_config,
                        title = '[Edibles Tank Car]',
                        roster = 'brit',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1988,
                        vehicle_life = 40,
                        speedy = True,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            weight = 30,
                            vehicle_length = 8))

    options = {'template': 'edibles_tank_car_brit_gen_3_template.png'}

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
                        title = '[Edibles Tank Car]',
                        roster = 'soam',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1905,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 6))

    options = {'template': 'edibles_tank_car_soam_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    # no gen 2 for edibles tank cars - straight to gen 3

    consist = WagonConsist(type_config = type_config,
                        title = '[Edibles Tank Car]',
                        roster = 'soam',
                        wagon_generation = 3,
                        replacement_id = '-none',
                        intro_date = 1988,
                        vehicle_life = 40,
                        speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 30,
                            vehicle_length = 8))

    options = {'template': 'edibles_tank_car_soam_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


