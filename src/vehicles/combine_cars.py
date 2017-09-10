import global_constants
from train import CombineConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CombineConsist(title = '[Combine Car]',
                           roster = 'pony',
                           base_numeric_id = 1000,
                           wagon_generation = 1,
                           intro_date = 1860,
                           vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_mail = 20,
                            capacity_freight = 12,
                            weight = 34,
                            vehicle_length = 5,
                            spriterow_num = 0))

    consist.add_unit(Wagon(consist = consist,
                            capacity_pax = 40,
                            weight = 34,
                            vehicle_length = 5,
                            spriterow_num = 1))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------
