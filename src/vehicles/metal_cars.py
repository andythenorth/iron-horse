import global_constants
from train import MetalConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = MetalConsist(title = '[Metal Car]',
                           roster = 'pony',
                           base_numeric_id = 890,
                           wagon_generation = 1,
                           intro_date = 1860,
                           vehicle_life = 50,
                           suppress_animated_pixel_warnings = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            weight = 30,
                            vehicle_length = 5,
                            spriterow_num = 0))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MetalConsist(title = '[Metal Car]',
                           roster = 'pony',
                           base_numeric_id = 900,
                           wagon_generation = 2,
                           intro_date = 1910,
                           vehicle_life = 50,
                           suppress_animated_pixel_warnings = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 60,
                            weight = 60,
                            vehicle_length = 9,
                            spriterow_num = 0))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MetalConsist(title = '[Metal Car]',
                           roster = 'pony',
                           base_numeric_id = 910,
                           wagon_generation = 3,
                           intro_date = 1960,
                           vehicle_life = 50,
                           suppress_animated_pixel_warnings = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 90,
                            weight = 90,
                            vehicle_length = 10,
                            spriterow_num = 0))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)
