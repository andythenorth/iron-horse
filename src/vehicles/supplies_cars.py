import global_constants
from train import SuppliesConsist, Wagon, GraphicsProcessorFactory

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SuppliesConsist(title = '[Supplies Car]',
                          roster = 'pony',
                          base_numeric_id = 710,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40,
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           weight = 6,
                           vehicle_length = 7))

    # Ho Ho, supplies cars will vary load graphics according to *build date of wagon*
    # not strictly right, but eh, means it got done :)

    options = {'template': 'supplies_car_pony_gen_1_template_0.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=1910,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=1910,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

    options = {'template': 'supplies_car_pony_gen_1_template_1.png'}

    consist.add_model_variant(intro_date=1910,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=2,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=1910,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=3,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    consist = SuppliesConsist(title = '[Supplies Car]',
                          roster = 'pony',
                          base_numeric_id = 700,
                          wagon_generation = 2,
                          intro_date = 1960,
                          vehicle_life = 40,)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 45,
                           weight = 12,
                           vehicle_length = 10))

    options = {'template': 'supplies_car_pony_gen_2_template_0.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=2010,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=2010,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

    options = {'template': 'supplies_car_pony_gen_2_template_1.png'}

    consist.add_model_variant(intro_date=2010,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=2,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=2010,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=3,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

    #--------------- antelope ----------------------------------------------------------------------

    consist = SuppliesConsist(title = '[Supplies Car]',
                          roster = 'antelope',
                          base_numeric_id = 2160,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40,
                          use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 6,
                            vehicle_length = 7))

    # Ho Ho, supplies cars will vary load graphics according to *build date of wagon*
    # not strictly right, but eh, means it got done :)

    options = {'template': 'supplies_car_ng_antelope_gen_1_template_0.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=1910,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=1910,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))

    options = {'template': 'supplies_car_ng_antelope_gen_1_template_1.png'}

    consist.add_model_variant(intro_date=1910,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=2,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=1910,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=3,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))


    #--------------- llama ----------------------------------------------------------------------


