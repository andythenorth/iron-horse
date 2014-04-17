import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

options = {'template': 'box_car_brit_gen_1_template.png',
           'recolour_map': {198: 40, 199: 41, 200: 42, 201: 43, 202: 44, 203: 45, 204: 46, 205: 47}}
graphics_processor_1 = GraphicsProcessorFactory('simple_recolour_pipeline', options)

options = {'template': 'box_car_brit_gen_1_template.png',
           'recolour_map': {198: 88, 199: 89, 200: 90, 201: 91, 202: 92, 203: 93, 204: 94, 205: 96}}
graphics_processor_2 = GraphicsProcessorFactory('simple_recolour_pipeline', options)

type_config = TypeConfig(base_id = 'box_car',
                    template = 'train.pynml',
                    class_refit_groups = ['packaged_freight'],
                    label_refits_allowed = ['GRAI', 'WHEA', 'MAIZ'],
                    label_refits_disallowed = [],
                    autorefit = True,
                    default_cargo = 'GOOD',
                    default_capacity_type = 'capacity_freight',
                    str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1860,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 20,
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


consist = WagonConsist(type_config = type_config,
                    title = 'Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1940,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 35,
                        weight = 18,
                        vehicle_length = 6,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


consist = WagonConsist(type_config = type_config,
                    title = 'Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 3,
                    replacement_id = '-none',
                    intro_date = 1995,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 55,
                        weight = 25,
                        vehicle_length = 8,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


type_config = TypeConfig(base_id = 'box_car_ng',
                template = 'train.pynml',
                class_refit_groups = ['packaged_freight'],
                label_refits_allowed = ['MAIL', 'GRAI', 'WHEA', 'MAIZ'],
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GOOD',
                default_capacity_type = 'capacity_freight',
                track_type = 'NG',
                  str_type_info = 'DOGTRACK')

consist = WagonConsist(type_config = type_config,
                    title = 'Narrow Gauge Box [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 1,
                    replacement_id = '-none',
                    intro_date = 1870,
                    vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 12,
                        capacity_mail = 12,
                        weight = 6,
                        vehicle_length = 4,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
