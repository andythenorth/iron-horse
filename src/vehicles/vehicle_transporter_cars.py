import global_constants
from train import VehicleTransporterConsist, Wagon, GraphicsProcessorFactory

def main():
    #--------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3

    consist = VehicleTransporterConsist(title = '[Vehicle Transporter Car]',
                                    roster = 'pony',
                                    base_numeric_id = 1530,
                                    wagon_generation = 3,
                                    replacement_id = '-none',
                                    intro_date = 1960,
                                    vehicle_life = 40,
                                    use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 12,
                            vehicle_length = 7))

    options = {'template': 'vehicle_transporter_car_pony_gen_3_template.png'}

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0,
                           graphics_processor=GraphicsProcessorFactory('pass_through_pipeline', options))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=1,
                           graphics_processor=GraphicsProcessorFactory('swap_company_colours_pipeline', options))
