import global_constants
from train import VehicleTransporterConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = VehicleTransporterConsist(roster='pony',
                                        base_numeric_id=1530,
                                        gen=3,
                                        subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=7)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])
