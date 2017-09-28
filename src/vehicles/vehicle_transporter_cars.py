import global_constants
from train import VehicleTransporterConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = VehicleTransporterConsist(title = '[Vehicle Transporter Car]',
                                    roster = 'pony',
                                    base_numeric_id = 1530,
                                    wagon_generation = 3,
                                     intro_date = 1960,
                                    vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            vehicle_length = 7))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
