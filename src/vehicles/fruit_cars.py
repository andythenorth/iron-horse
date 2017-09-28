import global_constants
from train import FruitConsist, FreightCar


def main():
    #--------------- antelope ----------------------------------------------------------------------
    consist = FruitConsist(roster='antelope',
                           base_numeric_id=2140,
                           vehicle_generation=1,
                           track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    consist = FruitConsist(roster='antelope',
                           base_numeric_id=2170,
                           vehicle_generation=2,
                           track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])

    consist = FruitConsist(roster='antelope',
                           base_numeric_id=2180,
                           vehicle_generation=3,
                           track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              graphics_processor=consist.graphics_processors['swap_company_colours'])
