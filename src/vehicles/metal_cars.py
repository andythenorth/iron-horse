import global_constants
from train import MetalConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = MetalConsist(roster='pony',
                           base_numeric_id=890,
                           gen=1,
                           subtype='A',
                           suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=5,
                     spriterow_num=0)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = MetalConsist(roster='pony',
                           base_numeric_id=900,
                           gen=2,
                           subtype='A',
                           suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     capacity=60,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = MetalConsist(roster='pony',
                           base_numeric_id=910,
                           gen=3,
                           subtype='A',
                           suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = MetalConsist(roster='pony',
                           base_numeric_id=2670,
                           gen=4,
                           subtype='A',
                           suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = MetalConsist(roster='pony',
                           base_numeric_id=2160,
                           gen=5,
                           subtype='A',
                           suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = MetalConsist(roster='pony',
                           base_numeric_id=2900,
                           gen=6,
                           subtype='A',
                           suppress_animated_pixel_warnings=True)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)
