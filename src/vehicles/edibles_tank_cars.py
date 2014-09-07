import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

options = {'template': 'edibles_tank_car_brit_gen_1_template.png'}
graphics_processor_1 = GraphicsProcessorFactory('pass_through_pipeline', options)
graphics_processor_2 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)

# tank cars are unrealistically autorefittable, and at no cost
# Pikka: if people complain that it's unrealistic, tell them "don't do it then"

type_config = TypeConfig(base_id = 'edibles_tank_car',
                template = 'train.pynml',
                class_refit_groups = ['liquids'],
                label_refits_allowed = [],
                label_refits_disallowed = global_constants.disallowed_refits_by_label['non_edible_liquids'],
                autorefit = True,
                default_cargo = 'WATR',
                default_capacity_type = 'capacity_freight')

        # mappings are to rows in the spritesheet, 0-based (0 is also default)
        # also get the allowed label refits from the graphics mapping - use row 0 if there's no specific graphics for the label

consist = WagonConsist(type_config = type_config,
                    title = 'Edibles Tank [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1925,
                    vehicle_life = 40,
                    speedy = True,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 25,
                        weight = 12,
                        vehicle_length = 5,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor=graphics_processor_1)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1,
                       graphics_processor=graphics_processor_2)

# no gen 2 for edibles tank cars - straight to gen 3

options = {'template': 'edibles_tank_car_brit_gen_3_template.png'}
graphics_processor_1 = GraphicsProcessorFactory('pass_through_pipeline', options)
graphics_processor_2 = GraphicsProcessorFactory('swap_company_colours_pipeline', options)

consist = WagonConsist(type_config = type_config,
                    title = 'Edibles Tank [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 3,
                    replacement_id = '-none',
                    intro_date = 1988,
                    vehicle_life = 40,
                    speedy = True,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 40,
                        weight = 30,
                        vehicle_length = 8,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor=graphics_processor_1)

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1,
                       graphics_processor=graphics_processor_2)
