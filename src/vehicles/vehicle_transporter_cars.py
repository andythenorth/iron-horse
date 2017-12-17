from train import VehicleTransporterCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = VehicleTransporterCarConsist(roster='pony',
                                        base_numeric_id=1530,
                                        gen=3,
                                        subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=7)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])
