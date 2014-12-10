import global_constants
import graphics_processor.utils as graphics_utils
from train import TypeConfig, WagonConsist, Wagon, GraphicsProcessorFactory

cargo_graphics_mappings = {}

recolour_maps = graphics_utils.get_container_recolour_maps()
graphics_options = {'template': 'intermodal_flat_car_brit_gen_3_template.png',
                    'recolour_maps': (recolour_maps),
                    'copy_block_top_offset': 30,
                    'num_rows_per_unit': 2,
                    'num_unit_types': 1}
graphics_processor_1 = GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options)

type_config = TypeConfig(base_id = 'intermodal_flat_car',
                template = 'car_with_visible_cargo.pynml',
                num_cargo_rows = 3,
                generic_cargo_rows = [0, 1, 2],
                class_refit_groups = ['express_freight', 'packaged_freight'],
                cargo_graphics_mappings = cargo_graphics_mappings,
                #label_refits_allowed = cargo_graphics_mappings.keys(),
                # maintain other sets (e.g. Squid etc) when changing container refits
                label_refits_allowed = ['FRUT','WATR'],
                label_refits_disallowed = ['FISH','LVST','OIL_','TOUR','WOOD'],
                autorefit = True,
                default_cargo = 'GOOD',
                default_capacity_type = 'capacity_freight')

consist = WagonConsist(type_config = type_config,
                    title = '[Intermodal Flat Car]',
                    vehicle_set = 'brit',
                    wagon_generation = 3,
                    replacement_id = '-none',
                    intro_date = 1960,
                    vehicle_life = 40,
                    speedy = True,
                    graphics_status = '',
                    use_legacy_spritesheet = True)

consist.add_unit(Wagon(type_config = type_config,
                        consist = consist,
                        capacity_freight = 48, # matched to RH and Squid containers
                        weight = 20,
                        vehicle_length = 8,
                        loading_speed = 25))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor = graphics_processor_1)
