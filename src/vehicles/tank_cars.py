import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

# tank cars are unrealistically autorefittable, and at no cost
# Pikka: if people complain that it's unrealistic, tell them "don't do it then"
type_config_normal = TypeConfig(base_id = 'tank_car',
                                template = 'train.pynml',
                                class_refit_groups = ['liquids'],
                                label_refits_allowed = [],
                                label_refits_disallowed = global_constants.disallowed_refits_by_label['edible_liquids'],
                                autorefit = True,
                                default_cargo = 'OIL_',
                                default_capacity_type = 'capacity_freight',
                                loading_speed_multiplier = 2)

type_config_narrow = TypeConfig(base_id = 'tank_car_ng',
                                template = 'train.pynml',
                                class_refit_groups = ['liquids'],
                                label_refits_allowed = [],
                                label_refits_disallowed = global_constants.disallowed_refits_by_label['edible_liquids'],
                                autorefit = True,
                                default_cargo = 'OIL_',
                                default_capacity_type = 'capacity_freight',
                                loading_speed_multiplier = 2,
                                track_type = 'NG')

def main():
    #--------------- brit ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Tank Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'tank_car_brit_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Tank Car]',
                        roster = 'brit',
                        wagon_generation = 2,
                        replacement_id = '-none',
                        intro_date = 1960,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            weight = 27,
                            vehicle_length = 8))

    options = {'template': 'tank_car_brit_gen_2_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_narrow,
                        title = '[Tank Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    options = {'template': 'tank_car_ng_brit_gen_1_template.png'}

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            weight = 4,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- soam ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config_normal,
                        title = '[Tank Car]',
                        roster = 'soam',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 12,
                            vehicle_length = 5))

    options = {'template': 'tank_car_soam_gen_1_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = WagonConsist(type_config = type_config_narrow,
                        title = '[Tank Car]',
                        roster = 'soam',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40)

    options = {'template': 'tank_car_ng_soam_gen_1_template.png'}

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 4,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))
