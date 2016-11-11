import global_constants
from train import CombineConsist, CombineCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CombineConsist(title = '[Combine Car]',
                           roster = 'pony',
                           base_numeric_id = 1000,
                           wagon_generation = 1,
                                        intro_date = 1860,
                           vehicle_life = 40)

    consist.add_unit(CombineCar(consist = consist,
                            capacity_mail = 20,
                            capacity_freight = 12,
                            capacity_pax = 30,
                            weight = 34,
                            vehicle_length = 9))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------
