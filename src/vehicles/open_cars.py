import global_constants
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

cargo_graphics_mappings = {'AORE': [1], 'COAL': [2], 'SAND': [3], 'CORE': [4], 'LIME': [5],
                           'SCMT': [6], 'IORE': [7], 'GRVL': [8], 'FRUT': [9], 'FRVG': [9],
                           'GRAI': [10], 'WHEA': [10], 'MAIZ': [10], 'FICR': [11],
                           'SGCN': [11], 'OLSD': [12], 'CLAY': [13]}

options = {'template': 'open_car_brit_gen_1_template.png',
           'recolour_map': {170: 186, 171: 187, 172: 188, 173: 189}}
graphics_processor_1 = GraphicsProcessorFactory('simple_recolour_pipeline', options)

options = {'template': 'open_car_brit_gen_1_template.png',
           'recolour_map': {170: 206, 171: 207, 172: 208, 173: 209}}
graphics_processor_2 = GraphicsProcessorFactory('simple_recolour_pipeline', options)

type_config = TypeConfig(base_id = 'open_car',
                template = 'car_with_visible_cargo.pynml',
                  num_cargo_rows = 14,
                class_refit_groups = ['all_freight'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = cargo_graphics_mappings.keys() ,
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GOOD',
                default_capacity_type = 'capacity_freight')

consist = WagonConsist(type_config = type_config,
                    title = 'Open [Car]',
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
                        weight = 7,
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
                    title = 'Open [Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 2,
                    replacement_id = '-none',
                    intro_date = 1925,
                          vehicle_life = 40,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 35,
                        weight = 15,
                        vehicle_length = 6,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)


type_config = TypeConfig(base_id = 'open_car_ng',
                template = 'car_with_visible_cargo.pynml',
                  num_cargo_rows = 14,
                class_refit_groups = ['all_freight'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                label_refits_allowed = cargo_graphics_mappings.keys() ,
                label_refits_disallowed = [],
                autorefit = True,
                default_cargo = 'GOOD',
                default_capacity_type = 'capacity_freight',
                track_type = 'NG')

consist = WagonConsist(type_config = type_config,
                    title = 'Narrow Gauge Open [Car]',
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
                        weight = 3,
                        vehicle_length = 3,
                        loading_speed = 20))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
