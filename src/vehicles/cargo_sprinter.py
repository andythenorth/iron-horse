import graphics_processor.utils as graphics_utils
from train import EngineConsist, CargoSprinter, GraphicsProcessorFactory

# cargo_sprinter is full of special cases, lots of yak-shaving to get it done
# specifically here it doesn't use type_config because engines don't, but it behaves like a wagon for cargos

recolour_maps = graphics_utils.get_container_recolour_maps()
graphics_options = {'template': 'cargo_sprinter_template.png',
           'recolour_maps': (recolour_maps),
           'copy_block_top_offset': 0,
           'num_rows_per_unit': 3,
           'num_unit_types': 3}
graphics_processor_1 = GraphicsProcessorFactory('extend_spriterows_for_recoloured_cargos_pipeline', graphics_options)

consist = EngineConsist(id = 'cargo_sprinter',
                  base_numeric_id = 1100,
                  title = 'Cargo Sprinter [Diesel]',
                  replacement_id = '-none',
                  power = 1000,
                  speed = 100,
                  # cargo sprinter is hard to balance stats for, it needs to be fast, cheap, powerful
                  # after experiments, it's now balanced suited to express intermodal, reaching top speed quickly,
                  # rather than very marginal routes competing with RVs
                  # it's also balanced to add capacity by adding more cargo sprinter units,
                  # rather than adding more than 2 unpowered trailing wagons
                  # it doesn't make a good loco for unpowered consists, although one or two should be ok
                  type_base_buy_cost_points = -2, # dibble buy cost for game balance
                  type_base_running_cost_points = -30, # dibble running costs for game balance
                  intro_date = 1999,
                  vehicle_life = 40,
                  use_legacy_spritesheet = True)

consist.add_unit(CargoSprinter(consist = consist,
                               weight = 46,
                               vehicle_length = 7,
                               capacity_freight = 36, # matched to 1.5x standard Road Hog and Squid containers
                               num_random_cargo_variants = len(graphics_options['recolour_maps']),
                               cargos_with_tanktainer_graphics = ['BEER', 'MILK', 'WATR']),
                        repeat=2)

consist.add_model_variant(intro_date=0,
                       end_date=1986,
                       spritesheet_suffix=0,
                       graphics_processor = graphics_processor_1)
