import global_constants
from train import SuppliesConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SuppliesConsist(title = '[Supplies Car]',
                          roster = 'pony',
                          base_numeric_id = 710,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 30,
                           weight = 6,
                           vehicle_length = 7))

    # Ho Ho, supplies cars will vary load graphics according to *build date of wagon*
    # not strictly right, but eh, means it got done :)

    consist.add_model_variant(intro_date=0,
                           end_date=1910,
                           graphics_processor=consist.graphics_processors['pass_through_0'])

    consist.add_model_variant(intro_date=0,
                           end_date=1910,
                           graphics_processor=consist.graphics_processors['swap_company_colours_0'])

    consist.add_model_variant(intro_date=1910,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through_1'])

    consist.add_model_variant(intro_date=1910,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours_1'])


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

    consist.add_model_variant(intro_date=0,
                           end_date=2010,
                           graphics_processor=consist.graphics_processors['pass_through_0'])

    consist.add_model_variant(intro_date=0,
                           end_date=2010,
                           graphics_processor=consist.graphics_processors['swap_company_colours_0'])

    consist.add_model_variant(intro_date=2010,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through_1'])

    consist.add_model_variant(intro_date=2010,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours_1'])

    #--------------- antelope ----------------------------------------------------------------------

    consist = SuppliesConsist(title = '[Supplies Car]',
                          roster = 'antelope',
                          base_numeric_id = 2160,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 6,
                            vehicle_length = 7))

    # Ho Ho, supplies cars will vary load graphics according to *build date of wagon*
    # not strictly right, but eh, means it got done :)

    consist.add_model_variant(intro_date=0,
                           end_date=1910,
                           graphics_processor=consist.graphics_processors['pass_through_0'])

    consist.add_model_variant(intro_date=0,
                           end_date=1910,
                           graphics_processor=consist.graphics_processors['swap_company_colours_0'])

    consist.add_model_variant(intro_date=1910,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through_1'])

    consist.add_model_variant(intro_date=1910,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours_1'])


    #--------------- llama ----------------------------------------------------------------------


