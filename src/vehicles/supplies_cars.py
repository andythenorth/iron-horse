import global_constants
from train import SuppliesConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=710,
                              gen=1,
                              subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=7)

    # Ho Ho, supplies cars will vary load graphics according to *build date of wagon*
    # not strictly right, but eh, means it got done :)

    consist.add_model_variant(start_date=0,
                              end_date=1910,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=1910,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=1910,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist.add_model_variant(start_date=1910,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=700,
                              gen=2,
                              subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=2010,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=2010,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=2010,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist.add_model_variant(start_date=2010,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- antelope ----------------------------------------------------------------------

    consist = SuppliesConsist(roster='antelope',
                              base_numeric_id=2160,
                              gen=1,
                              subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=7)

    # Ho Ho, supplies cars will vary load graphics according to *build date of wagon*
    # not strictly right, but eh, means it got done :)

    consist.add_model_variant(start_date=0,
                              end_date=1910,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=1910,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=1910,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    consist.add_model_variant(start_date=1910,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors[1])

    #--------------- llama ----------------------------------------------------------------------
